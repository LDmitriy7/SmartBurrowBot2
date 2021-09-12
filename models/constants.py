from aiogram.utils.helper import Helper, HelperMode, Item


class SendTo(Helper):
    mode = HelperMode.lowercase

    CHANNEL = Item()
    WORKER = Item()
