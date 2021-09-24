from aiogram.types import InlineKeyboardMarkup

from aiogram_utils.keyboards import InlineKeyboardButton


class Deposit(InlineKeyboardMarkup):
    INVOICE_URL = InlineKeyboardButton('Оплатить заявку', url='{invoice_url}')
    CHECK = InlineKeyboardButton('Подтвердить оплату', callback_data='deposit:check:{order_id}')

    def __init__(self, invoice_url: str, order_id: str):
        super().__init__(row_width=1)

        self.add(
            self.INVOICE_URL.format(invoice_url=invoice_url),
            self.CHECK.format(order_id=order_id),
        )
