from aiogram.types import ReplyKeyboardMarkup

from models import constants


class CancelBack(ReplyKeyboardMarkup):
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.BACK, self.CANCEL,
        )


class MissBack(ReplyKeyboardMarkup):
    MISS = constants.Fallbacks.MISS
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.row(self.MISS)

        self.add(
            self.BACK, self.CANCEL,
        )


class ReadyBack(ReplyKeyboardMarkup):
    READY = constants.Fallbacks.READY
    RESET = constants.Fallbacks.RESET
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.READY, self.RESET,
            self.BACK, self.CANCEL,
        )


class SaveBack(ReplyKeyboardMarkup):
    SAVE = constants.Fallbacks.SAVE
    RESET = constants.Fallbacks.RESET
    BACK = constants.Fallbacks.BACK
    CANCEL = constants.Fallbacks.CANCEL

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.SAVE, self.RESET,
            self.BACK, self.CANCEL,
        )
