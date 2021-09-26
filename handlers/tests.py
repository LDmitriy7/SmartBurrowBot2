from aiogram import types

import config
import texts
from loader import dp


@dp.message_handler(commands='test1', user_id=config.Users.ADMINS_IDS)
async def test1(msg: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.row(
        types.InlineKeyboardButton('test1', callback_data='test1'),
    )
    await msg.answer('...', reply_markup=kb)


@dp.callback_query_handler(text='test1', user_id=config.Users.ADMINS_IDS)
async def test1(query: types.CallbackQuery):
    await query.answer(texts.check_subscription_error, show_alert=True)
