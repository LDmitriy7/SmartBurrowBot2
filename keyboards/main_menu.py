from aiogram.types import ReplyKeyboardMarkup


class MainMenu(ReplyKeyboardMarkup):
    CREATE_ORDER = 'Создать заказ ➕'
    PERSONAL_ORDER = 'Личный заказ 🤝'
    MY_ORDERS = 'Мои заказы 💼'
    BALANCE = 'Баланс 🤑'
    REF_PROGRAM = '❗Реф. программа❗'
    GUIDE = 'Инструкция 📑'
    WORKER_MENU = 'Меню исполнителя'

    def __init__(self):
        super().__init__(resize_keyboard=True, row_width=2)

        self.add(
            self.CREATE_ORDER, self.PERSONAL_ORDER,
            self.MY_ORDERS, self.BALANCE,
            self.REF_PROGRAM, self.GUIDE,
            self.WORKER_MENU,
        )
