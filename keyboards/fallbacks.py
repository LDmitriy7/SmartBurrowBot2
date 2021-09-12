from aiogram.types import ReplyKeyboardMarkup


class BackCancel(ReplyKeyboardMarkup):
    BACK = 'Назад'
    CANCEL = 'Отменить'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.BACK, self.CANCEL,
        )
