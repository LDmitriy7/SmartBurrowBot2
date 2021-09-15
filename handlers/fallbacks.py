from __future__ import annotations

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup

import api
import commands
import keyboards as kb
import texts
from loader import dp
from models import constants


@dp.message_handler(button=constants.Fallbacks.CANCEL, state='*')
@dp.message_handler(commands=commands.CANCEL, state='*')
async def cancel(msg: types.Message, state: FSMContext):
    if msg.chat.type == types.ChatType.PRIVATE:
        reply_markup = kb.MainMenu()
    else:
        reply_markup = None

    await state.finish()
    await msg.answer(texts.cancelled, reply_markup=reply_markup)


@dp.message_handler(button=constants.Fallbacks.BACK, state='*')
async def back(msg: types.Message, state: FSMContext):
    current_state_name = await state.get_state()

    for _StatesGroup in StatesGroup.__subclasses__():
        if current_state_name in _StatesGroup.all_states_names:
            previous_state_name = await _StatesGroup.previous()
            if previous_state_name is None:
                await cancel(msg, state)
            else:
                await api.answer_for_state()

            break

# @dp.message_handler(button=[kb.BACK, kb.CANCEL], state=ChangeProfile)
# async def go_back_in_worker_menu():
#     on_conv_exit = QuestText('Отменено', kb.for_worker)
#     return UpdateData(new_state='previous', on_conv_exit=on_conv_exit)


# @dp.message_handler(button=kb.for_worker.BACK)
# async def go_back_in_main_menu():
#     on_conv_exit = QuestText('*Меню заказчика*:', kb.main)
#     return UpdateData(new_state='previous', on_conv_exit=on_conv_exit)


# @dp.callback_query_handler(text=kb.DEL_MESSAGE, state='*')
# async def delete_msg(msg: types.Message):
#     await msg.delete()
