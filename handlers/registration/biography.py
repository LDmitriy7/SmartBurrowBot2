from aiogram import types
from aiogram_utils.storage_proxy import StorageProxy

import api
import models
import states
from loader import dp

main_state = states.Registration.biography


@dp.message_handler(state=main_state)
async def process_biography(msg: types.Message):
    if len(msg.text) < 15:
        await msg.answer('Напиши не меньше 15 символов')
        return

    async with StorageProxy(models.Profile) as profile:
        profile.biography = msg.text

    await states.Registration.next()
    await api.answer_for_state()
