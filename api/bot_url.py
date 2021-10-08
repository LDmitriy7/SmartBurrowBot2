import config
from loader import dp


async def get_bot_url():
    me = await dp.bot.me
    return f'{config.TELEGRAM_BASE_URL}{me.username}'
