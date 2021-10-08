from contextlib import suppress

from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import config
from loader import dp

REF_PREFIX = 'ref-'

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'
CONFIG = 'config'

USER_COMMANDS = [
    types.BotCommand(START, 'Запустить бота'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(CANCEL, 'Отменить'),
    types.BotCommand(BROADCAST, 'Рассылка'),
]

DEVELOPERS_COMMANDS = ADMIN_COMMANDS + [
    types.BotCommand(CONFIG, 'Показать конфигурацию')
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)

    for user_id in config.Users.ADMINS_IDS:
        with suppress(TelegramAPIError):
            await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(user_id))

    for user_id in config.Users.DEVELOPERS_IDS:
        with suppress(TelegramAPIError):
            await dp.bot.set_my_commands(DEVELOPERS_COMMANDS, scope=types.BotCommandScopeChat(user_id))
