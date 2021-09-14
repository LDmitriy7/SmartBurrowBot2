from aiogram import types

import api
import keyboards as kb
import models
import states
from utils import StorageProxy
from loader import dp
from models.constants import SendTo


@dp.message_handler(text=kb.MainMenu.CREATE_ORDER, state='*')
async def entry_create_post(_msg: types.Message):
    async with StorageProxy(models.Order) as order:
        order.send_to = SendTo.CHANNEL

    await states.CreateOrder.first()
    await api.answer_for_state()

# TODO
# @dp.message_handler(text=kb.MainMenu.PERSONAL_ORDER)
# async def ask_user_role():
#     return QuestText(texts.personal_project.about, kb.user_roles)
#
#
# @dp.callback_query_handler(text=kb.user_roles.WORKER)
# async def send_invite_project_keyboard(msg: types.Message, user_id):
#     account = await users_db.get_account_by_id(user_id)
#     if account and account.profile:
#         text = 'Выберите *заказчика* из списка своих чатов'
#         await msg.edit_text(text, reply_markup=kb.choose_invite_chat)
#     else:
#         await msg.edit_text('Сначала пройдите регистрацию')
#         return UpdateData(new_state=RegistrationConv)
#
#
# @dp.inline_handler(button=kb.choose_invite_chat.INVITE_QUERY)
# async def send_project_invite_to_client(iquery: types.InlineQuery):
#     article = await funcs.form_invite_project_article()
#     await iquery.answer([article], cache_time=0, is_personal=True)
#
#
# @dp.callback_query_handler(text=kb.user_roles.CLIENT)
# async def entry_personal_project():
#     return UpdateData({'send_to': None}, new_state=CreateProjectConv)
#
#
# @dp.message_handler(button=kb.InviteProject.START_LINK, state='*')
# async def entry_personal_project_with_worker(user_id, suffix: str):
#     worker_id = int(suffix)
#     if user_id == worker_id:
#         return '*Вы сами не можете заполнить проект*'
#     return UpdateData({'worker_id': worker_id, 'send_to': SendTo.WORKER}, new_state=CreateProjectConv)
