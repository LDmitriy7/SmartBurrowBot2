from aiogram import types

import keyboards as kb
import texts
from loader import bot


async def ask_phone_number():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_phone_number, reply_markup=kb.PhoneNumber())


async def ask_email():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_email, reply_markup=kb.MissBack())


async def ask_biography():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_biography, reply_markup=kb.CancelBack())


async def ask_works():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_works, reply_markup=kb.SaveBack())


async def ask_subjects():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_subjects, reply_markup=kb.SaveBack())
    await bot.send_message(chat.id, '<b>Используй поиск</b>:', reply_markup=kb.SubjectsSearch())


async def ask_nickname():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_nickname, reply_markup=kb.CancelBack())
