from aiogram.types import ReplyKeyboardMarkup


class SendOrder(ReplyKeyboardMarkup):
    SEND = 'Отправить проект'
    BACK = 'Назад'
    CANCEL = 'Отменить'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.row(self.SEND)

        self.add(
            self.BACK, self.CANCEL,
        )
