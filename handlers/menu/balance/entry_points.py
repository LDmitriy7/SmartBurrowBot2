from aiogram import types

import keyboards as kb
import models
import texts
from loader import dp


@dp.message_handler(button=kb.MainMenu.BALANCE)
async def send_balance_info(msg: types.Message):
    user: models.User = models.User.objects(user_id=msg.from_user.id).first()
    await msg.answer(texts.balance_info.format(amount=user.balance), reply_markup=kb.Balance())

