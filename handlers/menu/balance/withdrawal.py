from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_utils.storage_proxy import StorageProxy

import api
import config
import keyboards as kb
import models
import states
import texts
from loader import dp


@dp.callback_query_handler(button=kb.Balance.WITHDRAW)
async def ask_withdrawal_amount(_query: types.CallbackQuery):
    await states.Withdrawal.first()
    await api.answer_for_state()


@dp.message_handler(state=states.Withdrawal.amount)
async def process_withdrawal_amount(msg: types.Message):
    if not msg.text.isdigit():
        await msg.answer('Ошибка, введи только число')
        return

    amount = int(msg.text)

    if amount <= 0:
        await msg.answer('Ошибка, отправь число больше нуля')
        return

    user: models.User = models.User.objects(user_id=msg.from_user.id).first()

    if amount > user.balance:
        await msg.answer('Ошибка, недостаточно денег на балансе')
        return

    async with StorageProxy(models.Withdrawal) as withdrawal:
        withdrawal.amount = amount

        if user.card_num:
            withdrawal.card_num = user.card_num
            await states.Withdrawal.confirmation.set()
        else:
            await states.Withdrawal.next()

    await api.answer_for_state()


@dp.message_handler(state=states.Withdrawal.card_num)
async def process_card_num(msg: types.Message):
    async with StorageProxy(models.Withdrawal) as withdrawal:
        withdrawal.card_num = msg.text

    user: models.User = models.User.objects(user_id=msg.from_user.id).first()
    user.card_num = msg.text
    user.save()

    await states.Withdrawal.next()
    await api.answer_for_state()


@dp.callback_query_handler(button=kb.ConfirmWithdrawal.CHANGE_CARD, state=states.Withdrawal.confirmation)
async def ask_new_card_num(_query: types.CallbackQuery):
    await states.Withdrawal.card_num.set()
    await api.answer_for_state()


@dp.callback_query_handler(button=kb.ConfirmWithdrawal.CONFIRM, state=states.Withdrawal.confirmation)
async def confirm_withdrawal(query: types.CallbackQuery, state: FSMContext):
    user: models.User = models.User.objects(user_id=query.from_user.id).first()
    withdrawal = await StorageProxy(models.Withdrawal).get_document()

    if user.balance < withdrawal.amount:
        await query.answer('Ошибка, недостаточно денег на балансе')
        return

    user.balance -= withdrawal.amount
    user.save()

    withdrawal.user_id = user.user_id
    withdrawal.save()

    await state.finish()
    await query.message.answer(texts.after_withdrawal, reply_markup=kb.MainMenu())
    await dp.bot.send_message(config.Users.OWNER_ID, texts.new_withdrawal)
