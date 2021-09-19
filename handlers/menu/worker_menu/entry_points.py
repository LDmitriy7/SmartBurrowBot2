from aiogram import types

import api
import keyboards as kb
import models
import states
import texts
from loader import dp


@dp.message_handler(button=kb.MainMenu.WORKER_MENU)
async def send_worker_menu(msg: types.Message):
    user: models.User = models.User.objects(user_id=msg.from_user.id).first()

    if not user.profile:
        await msg.answer(texts.ask_to_register)
        await states.Registration.first()
        await api.answer_for_state()
        return

    await msg.answer(texts.worker_menu_info, reply_markup=kb.WorkerMenu())
