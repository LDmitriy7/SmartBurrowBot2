from datetime import date

from aiogram import types

import keyboards as kb
import texts
from loader import bot


async def ask_work_type():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.create_order, reply_markup=kb.CancelBack())
    await bot.send_message(chat.id, texts.ask_work_type, reply_markup=kb.WorkTypes())


async def ask_subject():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_subject, reply_markup=kb.SubjectsSearch())


async def ask_date():
    chat = types.Chat.get_current()
    reply_markup = kb.Calendar(min_date=date.today(), current_date=date.today())
    await bot.send_message(chat.id, texts.ask_date, reply_markup=reply_markup)


async def ask_description():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_description, reply_markup=kb.CancelBack())


async def ask_price():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_price, reply_markup=kb.MissBack())


async def ask_note():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_note, reply_markup=kb.MissBack())
