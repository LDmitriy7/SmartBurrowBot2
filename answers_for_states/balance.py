from aiogram import types
from aiogram_utils.storage_proxy import StorageProxy

import keyboards as kb
import models
import texts
from loader import bot


async def ask_deposit_amount():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_deposit_amount, reply_markup=kb.CancelBack())


async def ask_withdrawal_amount():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_withdrawal_amount, reply_markup=kb.CancelBack())


async def ask_withdrawal_card_num():
    chat = types.Chat.get_current()
    await bot.send_message(chat.id, texts.ask_withdrawal_card_num, reply_markup=kb.CancelBack())


async def ask_withdrawal_confirmation():
    chat = types.Chat.get_current()

    async with StorageProxy(models.Withdrawal) as withdrawal:
        text = texts.ask_withdrawal_confirmation.format(
            amount=withdrawal.amount,
            card_num=withdrawal.card_num,
        )

    await bot.send_message(chat.id, text, reply_markup=kb.ConfirmWithdrawal())
