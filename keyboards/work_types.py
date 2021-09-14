from aiogram.types import InlineKeyboardMarkup

from utils.keyboards import InlineKeyboardButton


class WorkTypes(InlineKeyboardMarkup):
    _BUTTONS = [
        'Онлайн помощь', 'Домашняя работа', 'Лабораторная', 'Реферат', 'Курсовая',
        'Дипломная', 'Практика', 'Эссе', 'Доклад', 'Статья', 'Тезисы',
        'Презентация', 'Бизнес-план', 'Повысить уникальность'
    ]

    BUTTONS = [InlineKeyboardButton(b, callback_data=b) for b in _BUTTONS]

    def __init__(self):
        super().__init__(row_width=2)
        self.add(*self.BUTTONS)
