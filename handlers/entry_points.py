from typing import Optional

from aiogram import types
from aiogram.dispatcher import FSMContext

import commands
import keyboards as kb
import models
import texts
from loader import dp


def get_invited_by(msg: types.Message) -> Optional[int]:
    if not msg.get_args().startswith('ref-'):
        return None

    try:
        invited_by = int(msg.get_args().removeprefix('ref-'))
    except ValueError:
        return None
    else:
        if invited_by == msg.from_user.id:
            return None

    return invited_by


@dp.message_handler(commands=commands.START, state='*', chat_type=types.ChatType.GROUP)
async def send_commands_in_group(msg: types.Message):
    # keyboard = await funcs.get_group_keyboard() # TODO
    await msg.answer('Доступные команды:', reply_markup=None)


@dp.message_handler(commands=commands.START, state='*')
async def send_welcome(msg: types.Message, state: FSMContext):
    user = models.User.objects(user_id=msg.from_user.id).first()

    if not user:
        invited_by = get_invited_by(msg)
        models.User(user_id=msg.from_user.id, invited_by=invited_by).save()

    await state.finish()
    await msg.answer(texts.welcome, reply_markup=kb.MainMenu())
