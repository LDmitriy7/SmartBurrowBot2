from aiogram.types import ReplyKeyboardMarkup
from models import constants


class SendOrder(ReplyKeyboardMarkup):
    SEND = 'Отправить проект'
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.row(self.SEND)

        self.add(
            self.BACK, self.CANCEL,
        )
