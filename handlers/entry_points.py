import re
from typing import Optional

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

import keyboards as kb
import models
import texts
from loader import dp

REF_PREFIX = 'ref-'
REF_PREFIX_PATTERN = re.compile(f'^{REF_PREFIX}')


def get_invited_by(msg: types.Message) -> Optional[int]:
    if not msg.get_args().startswith(REF_PREFIX):
        return None

    try:
        invited_by = int(msg.get_args().removeprefix(REF_PREFIX))
    except ValueError:
        return None
    else:
        if invited_by == msg.from_user.id:
            return None

    return invited_by


# @dp.message_handler(CommandStart(''), state='*', chat_type=types.ChatType.GROUP)
# async def send_commands_in_group(msg: types.Message):
#     keyboard = await funcs.get_group_keyboard() # TODO
#     await msg.answer('Доступные команды:', reply_markup=None)


@dp.message_handler(CommandStart(''), state='*')
async def send_welcome(msg: types.Message, state: FSMContext):
    user = models.User.objects(user_id=msg.from_user.id).first()

    if not user:
        models.User(user_id=msg.from_user.id).save()

    await state.finish()
    await msg.answer(texts.welcome, reply_markup=kb.MainMenu())


@dp.message_handler(CommandStart(REF_PREFIX_PATTERN), state='*')
async def send_welcome_with_ref(msg: types.Message, state: FSMContext):
    user = models.User.objects(user_id=msg.from_user.id).first()

    if not user:
        invited_by = get_invited_by(msg)
        models.User(user_id=msg.from_user.id, invited_by=invited_by).save()

    await state.finish()
    await msg.answer(texts.welcome, reply_markup=kb.MainMenu())
