from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from aiogram_utils.storage_proxy import StorageProxy

main_state = states.Registration.works


@dp.message_handler(content_types=types.ContentType.PHOTO, state=main_state)
async def process_photo(msg: types.Message):
    async with StorageProxy(models.Profile) as profile:
        profile.works.append(msg.photo[-1].file_id)


@dp.message_handler(button=kb.SaveBack.RESET, state=main_state)
async def reset_works(msg: types.Message):
    async with StorageProxy(models.Profile) as profile:
        profile.works = []

    await msg.answer('Теперь отправляй фото заново')


@dp.message_handler(button=kb.SaveBack.SAVE, state=main_state)
async def save_works(_msg: types.Message):
    await states.Registration.next()
    await api.answer_for_state()
