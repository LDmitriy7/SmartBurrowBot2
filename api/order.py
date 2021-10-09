from __future__ import annotations

from aiogram import types

import models
from loader import bot


async def send_file(chat_id: int, file: models.File):
    if file.file_type == types.ContentType.PHOTO:
        await bot.send_photo(chat_id, file.file_id)
    elif file.file_type == types.ContentType.DOCUMENT:
        await bot.send_document(chat_id, file.file_id)
    else:
        raise ValueError('Unknown file type')


async def send_order_files(files: list[models.File], title='<b>Файлы к заказу:</b>', *, chat_id: int = None):
    chat_id = chat_id or types.Chat.get_current().id

    if files:
        await bot.send_message(chat_id, title)
        for f in files:
            await send_file(chat_id, f)
