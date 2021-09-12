from aiogram import types

import keyboards as kb
import texts
from loader import dp


@dp.message_handler(button=kb.MainMenu.GUIDE)
async def send_guide(msg: types.Message):
    await msg.answer(texts.guide, disable_web_page_preview=True)
