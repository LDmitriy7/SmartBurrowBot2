from aiogram import types
from aiogram.dispatcher import FSMContext

import api
import keyboards as kb
import models
import states
from loader import dp
from utils import StorageProxy

main_state = states.Registration.nickname


@dp.message_handler(state=main_state)
async def process_nickname(msg: types.Message, state: FSMContext):
    all_nicknames = api.get_all_nicknames()

    if msg.from_user.username and msg.from_user.username.lower() in msg.text.lower():
        await msg.answer('Пожалуйста, не используй свой юзернейм')
        return
    if msg.text in all_nicknames:
        await msg.answer('Этот никнейм уже занят')
        return

    async with StorageProxy(models.Profile) as profile:
        profile.nickname = msg.text

    user: models.User = models.User.objects(user_id=msg.from_user.id).first()
    user.profile = profile
    user.save()

    # await funcs.save_author_page()  # создание страницы автора TODO
    await state.finish()
    await msg.answer('Регистрация пройдена успешно', reply_markup=kb.WorkerMenu())
