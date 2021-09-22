from aiogram import types

import api
import config
import models
import states
import texts
from config.stop_words import STOP_WORDS
from loader import dp
from aiogram_utils.storage_proxy import StorageProxy

main_state = states.CreateOrder.description


@dp.message_handler(state=main_state)
async def process_description(msg: types.Message):
    if not (config.Order.MIN_DESCRIPTION_LEN < len(msg.text) < config.Order.MAX_DESCRIPTION_LEN):
        await msg.answer(texts.description_len_must_be)
        return

    require_approving = False

    if api.check_on_contacts(msg):
        require_approving = True

    for stop_word in STOP_WORDS:
        if stop_word.lower() in msg.text.lower():
            require_approving = True

    async with StorageProxy(models.Order) as order:
        order.description = msg.text
        order.require_approving = require_approving

    await states.CreateOrder.next()
    await api.answer_for_state()
