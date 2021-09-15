from datetime import date

from aiogram import types

import api
import keyboards as kb
import models
import texts
from loader import bot
from models import constants
from utils import StorageProxy


async def ask_work_type():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.create_order, reply_markup=kb.CancelBack())
    await bot.send_message(chat.id, texts.ask_work_type, reply_markup=kb.WorkTypes())


async def ask_subject():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_subject, reply_markup=kb.SubjectsSearch())


async def ask_until_date():
    chat = types.Chat.get_current()
    reply_markup = kb.Calendar(min_date=date.today(), current_date=date.today())
    await bot.send_message(chat.id, texts.ask_until_date, reply_markup=reply_markup)


async def ask_description():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_description, reply_markup=kb.CancelBack())


async def ask_price():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_price, reply_markup=kb.MissBack())


async def ask_note():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_note, reply_markup=kb.MissBack())


async def ask_files():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_files, reply_markup=kb.ReadyBack())


async def show_preview():
    chat = types.Chat.get_current()
    order = await StorageProxy(models.Order).get_object()

    if order.send_to == constants.SendTo.CHANNEL:
        await bot.send_message(chat.id, texts.ask_to_confirm_order)
    elif order.send_to == constants.SendTo.WORKER:
        await bot.send_message(chat.id, texts.ask_to_confirm_personal_order)
    else:
        await bot.send_message(chat.id, texts.ask_to_save_personal_order)

    post_text = api.get_order_post_text(order, with_note=True)
    await bot.send_message(chat.id, post_text, reply_markup=kb.SendOrder())
    await api.send_order_files(order.files)
