from aiogram.utils.helper import Helper, HelperMode, Item


class SendTo(Helper):
    mode = HelperMode.lowercase

    CHANNEL = Item()
    WORKER = Item()


class OrderStatus(Helper):
    mode = HelperMode.lowercase

    ACTIVE = Item()
    IN_PROGRESS = Item()
    COMPLETED = Item()


class Fallbacks(Helper):
    BACK = 'Назад'
    CANCEL = 'Отменить'
    READY = 'Готово'
    SAVE = 'Сохранить'
    RESET = 'Сбросить'
    MISS = 'Пропустить'
