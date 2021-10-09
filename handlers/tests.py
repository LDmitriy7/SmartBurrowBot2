import inspect

from aiogram import types

import config
import models
from loader import dp
import keyboards as kb


# @dp.message_handler(commands='test1', user_id=config.Users.ADMINS_IDS)
# async def test1(msg: types.Message):
#     kb = types.InlineKeyboardMarkup()
#     kb.row(
#         types.InlineKeyboardButton('test1', callback_data='test1'),
#     )
#     await msg.answer('...', reply_markup=kb)
#
#
# @dp.callback_query_handler(text='test1', user_id=config.Users.ADMINS_IDS)
# async def test1(query: types.CallbackQuery):
#     await query.answer(texts.check_subscription_error, show_alert=True)
#

@dp.message_handler(commands='config', user_id=config.Users.DEVELOPERS_IDS)
async def test2(msg: types.Message):
    def iter_members(_object):
        for _k, _v in inspect.getmembers(_object):
            if not _k.startswith('_'):
                yield _k, _v

    strings = []

    for k, v in iter_members(config):
        if inspect.ismodule(v):
            continue

        if inspect.isclass(v):
            strings.append(f'<b>[{v.__name__}]</b>')
            for k2, v2 in iter_members(v):
                strings.append(f'{k2} = {repr(v2)}')
        else:
            strings.append(f'{k} = {repr(v)}')

        strings.append('')

    await msg.answer('\n'.join(strings), disable_web_page_preview=True)


@dp.message_handler(commands='test3', user_id=config.Users.DEVELOPERS_IDS)
async def test3(msg: types.Message):
    await msg.answer(..., reply_markup=kb.SearchOrders(True))
    await msg.answer(..., reply_markup=kb.SearchOrders(False))


@dp.message_handler(commands='test4', user_id=config.Users.DEVELOPERS_IDS)
async def test4(msg: types.Message):
    with dp.bot.with_token(config.BrokerBot.TOKEN):
        await msg.answer('Hello, world')


@dp.message_handler(commands='test5', user_id=config.Users.DEVELOPERS_IDS, state='*')
async def test4(msg: types.Message):
    from .menu.create_order.preview import send_order_to_admin

    order = models.Order.objects().first()
    await send_order_to_admin(msg, order)
