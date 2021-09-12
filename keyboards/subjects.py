from aiogram.types import InlineKeyboardMarkup

from .tools import InlineKeyboardButton


class SubjectsSearch(InlineKeyboardMarkup):
    BY_WORDS = InlineKeyboardButton('Поиск по словам', switch_inline_query_current_chat='')
    MANUALLY = InlineKeyboardButton('Ручной поиск', callback_data='search_subjects_manually')

    def __init__(self):
        super().__init__(row_width=1)
        self.add(
            self.BY_WORDS,
            self.MANUALLY,
        )
