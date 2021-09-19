from aiogram.types import ReplyKeyboardMarkup


class WorkerMenu(ReplyKeyboardMarkup):
    MY_WORKS = 'Мои работы'
    SEARCH_ORDERS = 'Поиск заказов'
    MY_PROFILE = 'Мой профиль'
    MY_SUBJECTS = 'Мои предметы'
    BACK = 'Назад в меню заказчика'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.MY_WORKS, self.SEARCH_ORDERS,
            self.MY_PROFILE, self.MY_SUBJECTS,
            self.BACK,
        )
