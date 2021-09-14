from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.CreateOrder.price


@dp.message_handler(state=main_state)
async def process_price(msg: types.Message):
    if msg.text == kb.MissBack.MISS:
        price = None
    elif msg.text.isdigit():
        price = int(msg.text)
    else:
        await msg.answer('Ошибка, введи только число')
        return

    async with StorageProxy(models.Order) as order:
        order.price = price

    await states.CreateOrder.next()
    await api.answer_for_state()
