from aiogram import types
from aiogram_utils.storage_proxy import StorageProxy

import api
import keyboards as kb
import models
import states
import texts
from loader import dp
from models import constants


@dp.message_handler(button=kb.MainMenu.CREATE_ORDER, state='*')
async def entry_create_order(_msg: types.Message):
    async with StorageProxy(models.Order) as order:
        order.send_to = constants.SendTo.CHANNEL

    await states.CreateOrder.first()
    await api.answer_for_state()


@dp.message_handler(button=kb.MainMenu.PERSONAL_ORDER)
async def ask_user_role(msg: types.Message):
    await msg.answer(texts.personal_order.ask_user_role, reply_markup=kb.UserRoles())


@dp.callback_query_handler(button=kb.UserRoles.CLIENT)
async def entry_personal_order_as_client(_query: types.CallbackQuery):
    async with StorageProxy(models.Order) as order:
        order.send_to = None

    await states.CreateOrder.first()
    await api.answer_for_state()


@dp.callback_query_handler(button=kb.UserRoles.WORKER)
async def send_order_invite_keyboard(query: types.CallbackQuery):
    user: models.User = models.User.objects(user_id=query.from_user.id).first()

    if not user.profile:
        await query.message.edit_text('Сначала пройди регистрацию')
        await states.Registration.first()
        await api.answer_for_state()
        return

    await query.message.edit_text('Выберите <b>заказчика</b> из списка своих чатов',
                                  reply_markup=kb.PersonalOrderInvite())


@dp.inline_handler(button=kb.PersonalOrderInvite.CHOOSE_CHAT, state='*')
async def show_order_invite_article(query: types.InlineQuery):
    me = await dp.bot.me
    text = 'Перейдите по ссылке, чтобы заполнить персональный проект'
    keyboard = kb.OrderInvite(me.username, query.from_user.id)
    imc = types.InputMessageContent(message_text=text)

    article = types.InlineQueryResultArticle(
        id='0',
        title='Предложить проект',
        description='Нажмите, чтобы предложить личный заказ вашему собеседнику',
        input_message_content=imc,
        reply_markup=keyboard,
    )

    await query.answer([article], cache_time=0, is_personal=True)


@dp.message_handler(button=kb.OrderInvite.FILL_ORDER, state='*')
async def entry_personal_project_with_worker(msg: types.Message, button: dict):
    worker_id = int(button['worker_id'])

    if msg.from_user.id == worker_id:
        await msg.answer('<b>Ты сам не можешь заполнить проект</b>')
        return

    async with StorageProxy(models.Order) as order:
        order.send_to = constants.SendTo.WORKER
        order.worker_id = worker_id

    await states.CreateOrder.first()
    await api.answer_for_state()
