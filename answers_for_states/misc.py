from aiogram import types

import keyboards as kb
import texts
from loader import bot


async def ask_work_type():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.create_order, reply_markup=kb.BackCancel())
    await bot.send_message(chat.id, texts.ask_work_type, reply_markup=kb.WorkTypes())


async def ask_subject():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_subject, reply_markup=kb.SubjectsSearch())
