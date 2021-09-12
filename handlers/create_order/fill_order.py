from aiogram import types

import api
import keyboards as kb
import models
import states
from api.utils import StorageProxy
from loader import dp


@dp.callback_query_handler(button=kb.WorkTypes.BUTTONS, state=states.CreateOrder.work_type)
async def process_work_type(query: types.CallbackQuery):
    async with StorageProxy(models.Order) as order:
        order.work_type = query.data

    await states.CreateOrder.next()
    await api.answer_for_state()
