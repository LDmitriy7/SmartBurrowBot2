from aiogram import types

import keyboards as kb
import models
import texts
from loader import dp


@dp.message_handler(text=kb.WorkerMenu.SEARCH_ORDERS)
async def send_search_orders_options(msg: types.Message):
    user: models.User = models.User.objects(user_id=msg.from_user.id).first()
    reply_markup = kb.SearchOrders(user.broadcast_allowed)
    await msg.answer(texts.ask_search_orders_option, reply_markup=reply_markup)


@dp.callback_query_handler(button=kb.SearchOrders.SWITCH_BROADCAST)
async def switch_broadcast(query: types.CallbackQuery):
    user: models.User = models.User.objects(user_id=query.from_user.id).first()
    user.broadcast_allowed = not user.broadcast_allowed
    user.save()

    if user.broadcast_allowed:
        await query.answer('Теперь бот будет присылать тебе все заказы по выбранным предметам', show_alert=True)

    await query.message.edit_reply_markup(reply_markup=kb.SearchOrders(user.broadcast_allowed))


@dp.callback_query_handler(button=kb.SearchOrders.BY_SUBJECTS)
async def send_orders_by_subjects(query: types.CallbackQuery):
    user: models.User = models.User.objects(user_id=query.from_user.id).first()

    if not user.profile.subjects:
        await query.answer('Вы еще не выбрали ни одного предмета', show_alert=True)
        return

    # TODO:
    # orders = await api.get_orders_by_subjects(user.profile.subjects, show_expired=False)
    #
    # if orders:
    #     await query.message.answer('<b>Подходящие заказы:</b>')
    #     await api.send_projects(orders, pick_btn=True)
    # else:
    #     await query.message.answer('<b>Не найдено подходящих заказов</b>')
