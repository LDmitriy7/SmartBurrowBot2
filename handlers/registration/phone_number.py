from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from aiogram_utils.storage_proxy import StorageProxy

main_state = states.Registration.phone_number


@dp.message_handler(content_types=types.ContentType.CONTACT, state=main_state)
async def process_phone_number(msg: types.Message):
    async with StorageProxy(models.Profile) as profile:
        profile.phone_number = msg.contact.phone_number

    await states.Registration.next()
    await api.answer_for_state()


@dp.message_handler(button=kb.PhoneNumber.MISS, state=main_state)
async def skip_phone_number(_msg: types.Message):
    async with StorageProxy(models.Profile) as profile:
        profile.phone_number = None

    await states.Registration.next()
    await api.answer_for_state()


@dp.message_handler(state=main_state)
async def process_phone_number_manual(msg: types.Message):
    if not msg.text.isdigit() or len(msg.text) != 12:
        await msg.answer('Ошибка, введи только 12 цифр')
        return

    async with StorageProxy(models.Profile) as profile:
        profile.phone_number = msg.text

    await states.Registration.next()
    await api.answer_for_state()
