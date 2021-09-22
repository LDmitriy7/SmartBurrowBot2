from aiogram import types

import api
import keyboards as kb
import keyboards.personal_order
import models
import states
import texts
from loader import dp
from models.constants import SendTo
from aiogram_utils.storage_proxy import StorageProxy


@dp.message_handler(button=kb.MainMenu.CREATE_ORDER, state='*')
async def entry_create_order(_msg: types.Message):
    async with StorageProxy(models.Order) as order:
        order.send_to = SendTo.CHANNEL

    await states.CreateOrder.first()
    await api.answer_for_state()


@dp.message_handler(button=kb.MainMenu.PERSONAL_ORDER)
async def ask_user_role(msg: types.Message):
    await msg.answer(texts.personal_order.ask_user_role, reply_markup=keyboards.personal_order.UserRoles())


@dp.callback_query_handler(button=keyboards.personal_order.UserRoles.CLIENT)
async def entry_personal_order_as_client(_query: types.CallbackQuery):
    async with StorageProxy(models.Order) as order:
        order.send_to = None

    await states.CreateOrder.first()
    await api.answer_for_state()


@dp.callback_query_handler(button=keyboards.personal_order.UserRoles.WORKER)
async def send_order_invite_keyboard(query: types.CallbackQuery):
    user: models.User = models.User.objects(user_id=query.from_user.id).first()

    if not user.profile:
        await query.message.edit_text('Сначала пройди регистрацию')
        await states.Registration.first()
        await api.answer_for_state()
        return

    await query.message.edit_text('Выберите <b>заказчика</b> из списка своих чатов',
                                  reply_markup=kb.PersonalOrderInvite())

#
# @dp.inline_handler(button=kb.choose_invite_chat.INVITE_QUERY)
# async def send_project_invite_to_client(iquery: types.InlineQuery):
#     article = await funcs.form_invite_project_article()
#     await iquery.answer([article], cache_time=0, is_personal=True)
#
#


# @dp.message_handler(button=kb.InviteProject.START_LINK, state='*')
# async def entry_personal_project_with_worker(user_id, suffix: str):
#     worker_id = int(suffix)
#     if user_id == worker_id:
#         return '*Вы сами не можете заполнить проект*'
#     return UpdateData({'worker_id': worker_id, 'send_to': SendTo.WORKER}, new_state=CreateProjectConv)
