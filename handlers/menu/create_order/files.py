from aiogram import types

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.CreateOrder.files


@dp.message_handler(content_types=types.ContentType.PHOTO, state=main_state)
async def process_photo(msg: types.Message):
    async with StorageProxy(models.Order) as order:
        file = models.File(file_type=msg.content_type, file_id=msg.photo[-1].file_id)
        order.files.append(file)


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=main_state)
async def process_document(msg: types.Message):
    async with StorageProxy(models.Order) as order:
        file = models.File(file_type=msg.content_type, file_id=msg.document.file_id)
        order.files.append(file)


@dp.message_handler(button=kb.ReadyBack.RESET, state=main_state)
async def reset_files(msg: types.Message):
    async with StorageProxy(models.Order) as order:
        order.files = []

    await msg.answer('<b>Теперь отправляй файлы заново</b>')


@dp.message_handler(button=kb.ReadyBack.READY, state=main_state)
async def save_files(_msg: types.Message):
    await states.CreateOrder.next()
    await api.answer_for_state()
