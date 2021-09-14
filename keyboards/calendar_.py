from calendar import monthrange
from datetime import date, timedelta
from typing import Optional

from aiogram.types import InlineKeyboardMarkup

from utils.keyboards import InlineKeyboardButton

DAYS_OF_WEEK = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
MONTHS = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


class Calendar(InlineKeyboardMarkup):
    FAKE_BUTTON = InlineKeyboardButton('{text}', callback_data='calendar:fake_button')
    DATE = InlineKeyboardButton('{day_num}', callback_data='calendar:date:{iso_date}')
    NEXT_PAGE = InlineKeyboardButton('{text}', callback_data='calendar:next_page:{iso_date}')

    @staticmethod
    def get_header(current_date: date) -> str:
        return f'{MONTHS[current_date.month - 1]} {current_date.year}'

    @staticmethod
    def get_dates_rows(current_date: date) -> list[Optional[date]]:
        first_weekday, days_amount = monthrange(current_date.year, current_date.month)
        dates_rows = []

        for i in range(first_weekday):
            dates_rows.append(None)

        for i in range(1, days_amount + 1):
            dates_rows.append(current_date.replace(day=i))

        last_row_dates_amount = len(dates_rows) % 7

        for i in range((7 - last_row_dates_amount) % 7):
            dates_rows.append(None)

        return dates_rows

    @staticmethod
    def get_prev_month_date(current_date: date) -> date:
        return current_date.replace(day=1) - timedelta(days=1)

    @staticmethod
    def get_next_month_date(current_date: date) -> date:
        if current_date.month == 12:
            return current_date.replace(year=current_date.year + 1, month=1, day=1)
        return current_date.replace(year=current_date.year, month=current_date.month + 1, day=1)

    def make_date_button(self, button_date: Optional[date], min_date: date) -> InlineKeyboardButton:
        if not button_date or button_date < min_date:
            return self.FAKE_BUTTON.format(text=' ')
        return self.DATE.format(day_num=button_date.day, iso_date=button_date)

    def get_navigate_buttons(self, current_date: date, min_date: date) -> list[InlineKeyboardButton]:
        prev_month_date = self.get_prev_month_date(current_date)
        next_month_date = self.get_next_month_date(current_date)

        if prev_month_date >= min_date:
            turn_left_button = self.NEXT_PAGE.format(text='<<', iso_date=prev_month_date)
        else:
            turn_left_button = self.FAKE_BUTTON.format(text=' ')

        turn_right_button = self.NEXT_PAGE.format(text='>>', iso_date=next_month_date)
        middle_button = self.FAKE_BUTTON.format(text=' ')

        return [turn_left_button, middle_button, turn_right_button]

    def __init__(self, min_date: date, current_date: date):
        super().__init__(row_width=7)

        header_button = self.FAKE_BUTTON.format(text=self.get_header(current_date))
        days_of_week_buttons = [self.FAKE_BUTTON.format(text=d) for d in DAYS_OF_WEEK]
        dates_buttons = [self.make_date_button(d, min_date) for d in self.get_dates_rows(current_date)]
        navigate_buttons = self.get_navigate_buttons(current_date, min_date)

        self.row(header_button)
        self.row(*days_of_week_buttons)
        self.add(*dates_buttons)
        self.row(*navigate_buttons)
