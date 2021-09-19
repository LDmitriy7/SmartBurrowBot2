from aiogram.types import ReplyKeyboardMarkup

from models import constants
from utils.keyboards import KeyboardButton


class PhoneNumber(ReplyKeyboardMarkup):
    SEND = KeyboardButton('Отправить номер', request_contact=True)
    MISS = constants.Fallbacks.MISS
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.SEND, self.MISS,
            self.BACK, self.CANCEL,
        )
