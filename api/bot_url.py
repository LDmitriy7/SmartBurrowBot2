import config
from loader import dp


async def get_bot_url():
    me = await dp.bot.me
    return config.Urls.TELEGRAM_BASE.format(me.username)
