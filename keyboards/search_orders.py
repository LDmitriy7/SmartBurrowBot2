from aiogram.types import InlineKeyboardMarkup
from aiogram_utils.keyboards import InlineKeyboardButton
import config


class SearchOrders(InlineKeyboardMarkup):
    ALL = InlineKeyboardButton('Все заказы', url=config.Channel.URL)
    BY_SUBJECTS = InlineKeyboardButton('Только по выбранным предметам', callback_data='search_orders:by_subjects')
    SWITCH_BROADCAST = InlineKeyboardButton('{action}', callback_data='search_orders:switch_broadcast')

    def __init__(self, broadcast_allowed: bool):
        super().__init__(row_width=1)

        action = 'Выключить рассылку' if broadcast_allowed else 'Включить рассылку'

        self.add(
            self.ALL,
            self.BY_SUBJECTS,
            self.SWITCH_BROADCAST.format(action=action)
        )
