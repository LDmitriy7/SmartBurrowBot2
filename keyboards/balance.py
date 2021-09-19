from aiogram.types import InlineKeyboardMarkup

from utils.keyboards import InlineKeyboardButton


class Balance(InlineKeyboardMarkup):
    DEPOSIT = InlineKeyboardButton('Пополнить баланс', callback_data='balance:deposit')
    WITHDRAW = InlineKeyboardButton('Вывести деньги', callback_data='balance:withdraw')

    def __init__(self):
        super().__init__(row_width=1)

        self.add(
            self.DEPOSIT,
            self.WITHDRAW,
        )
