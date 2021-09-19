from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.parts import paginate

from config.subjects import SUBJECTS_BY_CATEGORY
from utils.keyboards import InlineKeyboardButton


class SubjectsSearch(InlineKeyboardMarkup):
    BY_WORDS = InlineKeyboardButton('Поиск по словам', switch_inline_query_current_chat='')
    MANUALLY = InlineKeyboardButton('Ручной поиск', callback_data='search_subjects:manually')

    def __init__(self):
        super().__init__(row_width=1)
        self.add(
            self.BY_WORDS,
            self.MANUALLY,
        )


class SubjectsCategories(InlineKeyboardMarkup):
    BUTTONS = sorted(SUBJECTS_BY_CATEGORY)

    def __init__(self):
        super().__init__(row_width=1)

        buttons = [InlineKeyboardButton(b, callback_data=b) for b in self.BUTTONS]
        self.add(*buttons)


class SubjectsInCategory(InlineKeyboardMarkup):
    NEXT_PAGE = InlineKeyboardButton('{text}', callback_data='subjects:next_page:{page_num}')
    BACK_TO_CATEGORIES = InlineKeyboardButton('Назад', callback_data='subjects:back_to_categories')

    @staticmethod
    def get_subjects_buttons(subjects: list[str], marked_subjects: list = ()) -> list[InlineKeyboardButton]:
        buttons = []

        for s in subjects:
            button = InlineKeyboardButton(s, callback_data=s)
            if s in set(marked_subjects):
                button.text += ' ✅'
            buttons.append(button)

        return buttons

    def __init__(self, category: str, page: int, marked_subjects: list = ()):
        super().__init__(row_width=1)

        sorted_category_subjects = sorted(SUBJECTS_BY_CATEGORY[category])
        subjects = list(paginate(sorted_category_subjects, page, limit=10))

        subjects_buttons = self.get_subjects_buttons(subjects, marked_subjects)
        self.add(*subjects_buttons)

        navigate_buttons = []

        if page > 0:
            turn_left_button = self.NEXT_PAGE.format(text='<<', page_num=page - 1)
            navigate_buttons.append(turn_left_button)

        navigate_buttons.append(self.BACK_TO_CATEGORIES)

        if sorted_category_subjects[-1] != subjects[-1]:
            turn_right_button = self.NEXT_PAGE.format(text='>>', page_num=page + 1)
            navigate_buttons.append(turn_right_button)

        self.row(*navigate_buttons)
