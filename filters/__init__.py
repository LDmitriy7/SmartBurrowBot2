import aiogram_utils

from loader import dp


def setup():
    aiogram_utils.filters.setup(dp)
