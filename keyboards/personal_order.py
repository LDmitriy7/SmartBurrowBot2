from aiogram.types import InlineKeyboardMarkup

from aiogram_utils.keyboards import InlineKeyboardButton


class UserRoles(InlineKeyboardMarkup):
    CLIENT = InlineKeyboardButton('Я заказчик', callback_data='user_roles:client')
    WORKER = InlineKeyboardButton('Я исполнитель', callback_data='user_roles:worker')

    def __init__(self):
        super().__init__(row_width=1)

        self.add(
            self.CLIENT,
            self.WORKER,
        )


class PersonalOrderInvite(InlineKeyboardMarkup):
    CHOOSE_CHAT = InlineKeyboardButton('Выбрать чат', switch_inline_query='Предложить проект')

    def __init__(self):
        super().__init__(row_width=1)

        self.add(self.CHOOSE_CHAT)
