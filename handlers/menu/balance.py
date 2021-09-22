"""Наборы всех обычных состояний бота."""
from aiogram import types

import keyboards as kb
import models
import texts
from loader import dp


# @QuestFunc
# async def ask_confirmation_withdrawal():
#     chat = types.Chat.get_current()
#     sdata = await dp.current_state().get_data()
#     text = f'Вывести {sdata["amount"]} грн. на карту {sdata["card_num"]}?'
#     await bot.send_message(chat.id, text, reply_markup=kb.confirm_withdrawal)
#
#
# class WithdrawMoney(ConvStatesGroup):
#     amount = ConvState(QuestText(texts.balance.ask_withdrawal_amount, kb.back))
#     card_num = ConvState(QuestText(texts.balance.ask_withdrawal_card_num, kb.back_cancel))
#     confirm = ConvState(ask_confirmation_withdrawal)
#

@dp.message_handler(button=kb.MainMenu.BALANCE)
async def send_balance_info(msg: types.Message):
    user: models.User = models.User.objects(user_id=msg.from_user.id).first()
    await msg.answer(texts.balance_info.format(amount=user.balance), reply_markup=kb.Balance())

#
# @dp.callback_query_handler(button=kb.balance.DEPOSIT_MONEY)
# async def deposit_money(msg: types.Message, user_id):
#     await msg.answer(texts.balance.for_withdrawing.format(user_id=user_id), reply_markup=kb.payment)
#
#
# @dp.callback_query_handler(button=kb.payment.CONFIRM)
# async def confirm_payment(query: types.CallbackQuery, user_id):
#     user_url = f'[{user_id}](tg://user?id={user_id})'
#     text = f'*Запрос на проверку оплаты от пользователя {user_url}:*'
#     await bot.send_message(config.Admins.MAIN_ADMIN_ID, text, reply_markup=kb.ControlUser(user_id))
#     await query.answer('Мы зачислим тебе деньги, как только проверим оплату', show_alert=True)
#
#
# @dp.callback_query_handler(button=kb.PaymentInChat.CONFIRM)
# async def confirm_payment_in_chat(query: types.CallbackQuery, user_id, suffix: str):
#     user_url = f'[{user_id}](tg://user?id={user_id})'
#     text = f'*Запрос на пополнение счета для оплаты проекта от пользователя {user_url}:*'
#     chat_id, project_price = map(int, suffix.split('_'))
#     await bot.send_message(config.Admins.MAIN_ADMIN_ID, text,
#                            reply_markup=kb.ControlUser2(user_id, chat_id, project_price))
#     await query.answer('Мы заключим эту сделку, как только проверим оплату', show_alert=True)
#
#
# @dp.callback_query_handler(text=kb.balance.WITHDRAW_MONEY)
# async def ask_withdraw_amount():
#     return UpdateData(new_state=WithdrawMoney)
#
#
# @dp.message_handler(state=WithdrawMoney.amount)
# async def process_withdraw(text: str):
#     if not text.isdigit():
#         return 'Ошибка, введите только число'
#
#     amount = int(text)
#     balance = await funcs.get_account_balance()
#
#     if not (0 < amount <= balance):
#         return 'Ошибка, недопустимая сумма'
#
#     card_num = await funcs.get_account_card_num()
#
#     if card_num:
#         return UpdateData({'amount': amount, 'card_num': card_num}, new_state=WithdrawMoney.confirm)
#     else:
#         return UpdateData({'amount': amount})
#
#
# @dp.message_handler(state=WithdrawMoney.card_num)
# async def process_card_num(user_id: int, text: str):
#     await users_db.update_account_card_num(user_id, text)
#     return UpdateData({'card_num': text})
#
#
# @dp.callback_query_handler(button=kb.ConfirmWithdrawal.CHANGE_CARD, state=WithdrawMoney.confirm)
# async def ask_new_card_num():
#     return UpdateData(new_state=WithdrawMoney.card_num)
#
#
# @dp.callback_query_handler(button=kb.ConfirmWithdrawal.CONFIRM, state=WithdrawMoney.confirm)
# async def process_card_num(user_id: int, sdata: dict):
#     amount, card_num = sdata['amount'], sdata['card_num']
#     await users_db.incr_balance(user_id, -amount)
#
#     withdrawal = data_models.Withdrawal(user_id, amount, card_num)
#     await users_db.add_withdrawal(withdrawal)
#     text = '*Поступил новый запрос на вывод средств*. Смотри в /withdrawals'
#     await bot.send_message(config.Admins.MAIN_ADMIN_ID, text)
#     return UpdateData(), QuestText(texts.balance.after_withdrawing, kb.main)
