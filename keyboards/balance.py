from aiogram.types import InlineKeyboardMarkup

from aiogram_utils.keyboards import InlineKeyboardButton


class Balance(InlineKeyboardMarkup):
    DEPOSIT = InlineKeyboardButton('Пополнить баланс', callback_data='balance:deposit')
    WITHDRAW = InlineKeyboardButton('Вывести деньги', callback_data='balance:withdraw')

    def __init__(self):
        super().__init__(row_width=1)

        self.add(
            self.DEPOSIT,
            self.WITHDRAW,
        )


class ConfirmWithdrawal(InlineKeyboardMarkup):
    CONFIRM = InlineKeyboardButton('Подтвердить вывод', callback_data='withdrawal:confirm')
    CHANGE_CARD = InlineKeyboardButton('Выбрать другую карту', callback_data='withdrawal:change_card')

    def __init__(self):
        super().__init__(row_width=1)

        self.add(
            self.CONFIRM,
            self.CHANGE_CARD,
        )
