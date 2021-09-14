from datetime import date

from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.CreateOrder.date


@dp.callback_query_handler(button=kb.Calendar.NEXT_PAGE, state=main_state)
async def show_next_page(query: types.CallbackQuery, button: dict):
    date_ = date.fromisoformat(button['iso_date'])
    reply_markup = kb.Calendar(min_date=date.today(), current_date=date_)
    await query.message.edit_reply_markup(reply_markup)


@dp.callback_query_handler(button=kb.Calendar.DATE, state=main_state)
async def process_date(query: types.CallbackQuery, button: dict):
    date_ = date.fromisoformat(button['iso_date'])

    async with StorageProxy(models.Order) as order:
        order.date = date_

    await states.CreateOrder.next()
    await query.answer(f'Выбрано: {api.format_date(date_)}')
    await api.answer_for_state()
