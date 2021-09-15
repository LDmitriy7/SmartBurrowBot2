from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import api
from models import constants
import keyboards as kb
from loader import dp
import states
import texts
import asyncio

main_state = states.CreateOrder.preview


@dp.message_handler(text=kb.confirm_project.SEND, state=States.confirm, sdata={'send_to': constants.SendTo.CHANNEL})
async def send_project_to_channel(user_id: int, sdata: dict):
    project = await funcs.save_project()

    if sdata.get('require_approving'):
        await funcs.send_post_to_admin(user_id, project.id, project.data)
        return UpdateData(), QuestText('Твой заказ будет опубликован после проверки админом', kb.main)
    else:
        post = await funcs.send_post(project.id, project.data)
        asyncio.create_task(funcs.broadcast_order(project.id, project.data))
        return UpdateData(), QuestText(texts.create_project.show_preview.format(post_url=post.url), kb.main)


@dp.message_handler(text=kb.confirm_project.SEND, state=States.confirm, sdata={'send_to': constants.SendTo.WORKER})
async def send_project_to_worker(msg: types.Message, user_name):
    project = await funcs.save_project()
    await msg.answer('Идет отправка...', reply_markup=kb.main)
    chats = await funcs.create_and_save_groups(project.client_id, project.worker_id, project.id)

    try:
        await funcs.send_chat_link_to_worker(user_name, project.worker_id, chats.worker_chat.link)
    except TelegramAPIError:
        text = 'Не могу отправить проект этому исполнителю'
    else:
        keyboard = kb.link_button('Перейти в чат', chats.client_chat.link)
        text = QuestText('Проект отправлен, ожидайте автора в чате', keyboard)
    return UpdateData(), text


@dp.message_handler(text=kb.confirm_project.SEND, state=States.confirm, sdata={'send_to': None})
async def send_offer_keyboard(msg: types.Message):
    project = await funcs.save_project()
    await msg.answer(texts.create_project.pre_ask_worker, reply_markup=kb.main)
    keyboard = kb.OfferProject(project.id)
    return UpdateData(), QuestText(texts.create_project.ask_worker, keyboard)


@dp.inline_handler(button=kb.OfferProject.OFFER)
async def send_offer_to_worker(iquery: types.InlineQuery, suffix: str):
    article = funcs.make_offer_project_article(suffix)
    await iquery.answer([article], cache_time=0, is_personal=True)
