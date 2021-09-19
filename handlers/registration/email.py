from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.Registration.email


@dp.message_handler(state=main_state)
async def process_email(msg: types.Message):
    if msg.text == kb.MissBack.MISS:
        email = None
    elif '@' in msg.text:
        email = msg.text
    else:
        await msg.answer('Похоже, вы ошиблись в email\'е')
        return

    async with StorageProxy(models.Profile) as profile:
        profile.email = email

    await states.Registration.next()
    await api.answer_for_state()
