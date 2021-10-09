from aiogram.types import InlineKeyboardMarkup
from aiogram_utils.keyboards import InlineKeyboardButton


class ModerateOrder(InlineKeyboardMarkup):
    APPROVE = InlineKeyboardButton('Опубликовать проект', callback_data='moderate_order:approve:{order_id}')
    REJECT = InlineKeyboardButton('Отклонить проект', callback_data='moderate_order:reject:{order_id}')

    def __init__(self, order_id: str):
        super().__init__(row_width=1)

        self.add(
            self.APPROVE.format(order_id=order_id),
            self.REJECT.format(order_id=order_id),
        )
