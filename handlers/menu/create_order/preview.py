from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_utils.storage_proxy import StorageProxy

import api
import config
import keyboards as kb
import models
import states
import texts
from loader import dp
from models import constants

main_state = states.CreateOrder.preview


@dp.message_handler(button=kb.SendOrder.SEND, state=main_state)
async def send_order(msg: types.Message, state: FSMContext):
    async with StorageProxy(models.Order) as order:
        order.client_id = msg.from_user.id
        order.save()

    if order.send_to == constants.SendTo.CHANNEL:
        if order.require_approving:
            await send_order_to_admin(msg, order)
        else:
            await send_order_to_channel(msg)
    elif order.send_to == constants.SendTo.WORKER:
        await send_order_to_worker(msg)
    else:
        await send_offer_order_keyboard(msg, order)

    # await state.finish()


async def send_offer_order_keyboard(msg: types.Message, order: models.Order):
    await msg.answer(texts.personal_order_saved, reply_markup=kb.MainMenu())
    await msg.answer(texts.ask_personal_order_worker, reply_markup=kb.OfferPersonalOrder(order.id))


@dp.inline_handler(button=kb.OfferPersonalOrder.CHOOSE_CHAT, state='*')
async def offer_order_to_worker(query: types.InlineQuery, button: dict):
    order_id: str = button['order_id']
    imc = types.InputMessageContent(message_text=texts.you_received_personal_order)

    article = types.InlineQueryResultArticle(
        id='0',
        title='Предложить проект',
        description='Нажмите, чтобы предложить личный заказ этому пользователю',
        input_message_content=imc,
        reply_markup=kb.PickPersonalOrder(order_id),
    )

    await query.answer([article], cache_time=0, is_personal=True)


async def send_order_to_admin(msg: types.Message, order: models.Order):
    post_text = api.get_order_post_text(order)
    reply_markup = kb.ModerateOrder(order.id)

    await dp.bot.send_message(config.Users.OWNER_ID, f'Проверьте заказ от {msg.from_user.get_mention()}:')
    await dp.bot.send_message(config.Users.OWNER_ID, post_text, reply_markup=reply_markup)
    await api.send_order_files(order.files, chat_id=config.Users.OWNER_ID)

    await msg.answer('Твой заказ будет опубликован после проверки админом', reply_markup=kb.MainMenu())


# async def send_order_to_channel(msg: types.Message):
#     post = await api.send_post(project.id, project.data)
#     asyncio.create_task(api.broadcast_order(project.id, project.data))
#
#     await msg.answer(texts.create_project.show_preview.format(post_url=post.url), reply_markup=kb.MainMenu())


async def send_order_to_worker(msg: types.Message, user_name, order: models.Order):
    await msg.answer('Идет отправка...', reply_markup=kb.MainMenu())
    chats = await api.create_and_save_groups(order.client_id, order.worker_id, order.id)

#     try:
#         await funcs.send_chat_link_to_worker(user_name, project.worker_id, chats.worker_chat.link)
#     except TelegramAPIError:
#         text = 'Не могу отправить проект этому исполнителю'
#     else:
#         keyboard = kb.link_button('Перейти в чат', chats.client_chat.link)
#         text = QuestText('Проект отправлен, ожидайте автора в чате', keyboard)
#     return UpdateData(), text
#
