from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.CreateOrder.note


@dp.message_handler(state=main_state)
async def process_note(msg: types.Message):
    if msg.text == kb.MissBack.MISS:
        note = None
    else:
        note = msg.text

    async with StorageProxy(models.Order) as order:
        order.note = note

    await states.CreateOrder.next()
    await api.answer_for_state()
