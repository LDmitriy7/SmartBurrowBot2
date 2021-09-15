import asyncio

from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import api
import keyboards as kb
import models
import states
import texts
from loader import dp
from models import constants
from utils import StorageProxy

main_state = states.CreateOrder.preview


@dp.message_handler(text=kb.SendOrder.SEND, state=main_state, sdata={'send_to': constants.SendTo.CHANNEL})
async def send_order(user_id: int, sdata: dict):
    async with StorageProxy(models.Order) as order:
        order.save()

    if order.send_to == constants.SendTo.CHANNEL:
        if order.require_approving:
            await send_order_to_admin()
        else:
            await send_order_to_channel()
    elif order.send_to == constants.SendTo.WORKER:
        await send_order_to_worker()
    else:
        await send_offer_keyboard()


async def send_order_to_admin(user_id: int, sdata: dict):
    await api.send_post_to_admin(user_id, project.id, project.data)
    return UpdateData(), QuestText('Твой заказ будет опубликован после проверки админом', kb.main)


async def send_order_to_channel():
    post = await api.send_post(project.id, project.data)
    asyncio.create_task(funcs.broadcast_order(project.id, project.data))
    return UpdateData(), QuestText(texts.create_project.show_preview.format(post_url=post.url), kb.main)


async def send_order_to_worker(msg: types.Message, user_name):
    await msg.answer('Идет отправка...', reply_markup=kb.MainMenu())
    chats = await funcs.create_and_save_groups(project.client_id, project.worker_id, project.id)

    try:
        await funcs.send_chat_link_to_worker(user_name, project.worker_id, chats.worker_chat.link)
    except TelegramAPIError:
        text = 'Не могу отправить проект этому исполнителю'
    else:
        keyboard = kb.link_button('Перейти в чат', chats.client_chat.link)
        text = QuestText('Проект отправлен, ожидайте автора в чате', keyboard)
    return UpdateData(), text


async def send_offer_keyboard(msg: types.Message):
    project = await funcs.save_project()
    await msg.answer(texts.create_project.pre_ask_worker, reply_markup=kb.main)
    keyboard = kb.OfferProject(project.id)
    return UpdateData(), QuestText(texts.create_project.ask_worker, keyboard)


@dp.inline_handler(button=kb.OfferProject.OFFER)
async def send_offer_to_worker(iquery: types.InlineQuery, suffix: str):
    article = funcs.make_offer_project_article(suffix)
    await iquery.answer([article], cache_time=0, is_personal=True)
#
