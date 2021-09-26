from aiogram import types
from aiogram.dispatcher import FSMContext

import api
import keyboards as kb
import models
import states
import texts
from loader import dp, merchant


@dp.callback_query_handler(button=kb.Balance.DEPOSIT)
async def ask_deposit_amount(_query: types.CallbackQuery):
    await states.Deposit.first()
    await api.answer_for_state()


@dp.message_handler(state=states.Deposit.amount)
async def process_deposit_amount(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Ошибка, введи только число')
        return

    amount = int(msg.text)

    if amount <= 0:
        await msg.answer('Ошибка, отправь число больше нуля')
        return

    deposit = models.Deposit(user_id=msg.from_user.id, amount=amount).save()

    my_msg = await msg.answer('Создаю ссылку для оплаты...')

    # bot_url = await api.get_bot_url()
    invoice_url = await merchant.get_invoice_url(str(deposit.id), deposit.amount)
    await my_msg.edit_text(texts.ask_to_pay, reply_markup=kb.Deposit(invoice_url, str(deposit.id)))

    await state.finish()
    await msg.answer(texts.deposit_info, reply_markup=kb.MainMenu())


@dp.callback_query_handler(button=kb.Deposit.CHECK, state='*')
async def check_deposit(query: types.CallbackQuery, button: dict):
    order_id = button['order_id']
    result = await merchant.check_payment(order_id)

    if not result:
        await query.answer('Платеж не найден')
        return

    deposit: models.Deposit = models.Deposit.objects(id=order_id).first()

    if deposit.credited:
        await query.answer('Баланс уже пополнен')
        return

    deposit.credited = True
    deposit.save()

    user: models.User = models.User.objects(user_id=deposit.user_id).first()
    user.balance += deposit.amount
    user.save()

    await query.answer('Баланс пополнен')
