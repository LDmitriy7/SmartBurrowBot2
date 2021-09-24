from aiogram import types

import api
import config
import models
from loader import dp, merchant
from models import documents


@dp.message_handler(commands='test1', user_id=config.Users.ADMINS_IDS)
async def test1(msg: types.Message):
    bot_url = await api.get_bot_url()
    deposit = documents.Deposit(user_id=msg.from_user.id, amount=100).save()
    invoice_url = await merchant.get_invoice_url(str(deposit.id), deposit.amount, bot_url)
    await msg.answer(str(deposit.id))
    await msg.answer(invoice_url)


@dp.message_handler(commands='test2', user_id=config.Users.ADMINS_IDS)
async def test2(msg: types.Message):
    order_id = msg.get_args()
    result = await merchant.check_payment(order_id)

    if not result:
        await msg.answer('Платеж не найден')
        return

    deposit: models.Deposit = documents.Deposit.objects(id=order_id).first()

    if deposit.credited:
        await msg.answer('Баланс уже пополнен')
        return

    deposit.credited = True
    deposit.save()

    user: models.User = documents.User.objects(user_id=deposit.user_id).first()
    user.balance += deposit.amount
    user.save()

    await msg.answer('Баланс пополнен')
