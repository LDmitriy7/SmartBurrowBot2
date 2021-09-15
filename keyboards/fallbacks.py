from aiogram.types import ReplyKeyboardMarkup


class CancelBack(ReplyKeyboardMarkup):
    BACK = 'Назад'
    CANCEL = 'Отменить'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.BACK, self.CANCEL,
        )


class MissBack(ReplyKeyboardMarkup):
    MISS = 'Пропустить'
    BACK = 'Назад'
    CANCEL = 'Отменить'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.row(self.MISS)

        self.add(
            self.BACK, self.CANCEL,
        )


class ReadyBack(ReplyKeyboardMarkup):
    READY = 'Готово'
    RESET = 'Сбросить'
    BACK = 'Назад'
    CANCEL = 'Отменить'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.READY, self.RESET,
            self.BACK, self.CANCEL,
        )
