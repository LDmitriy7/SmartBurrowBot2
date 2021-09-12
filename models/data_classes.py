from dataclasses import dataclass
from typing import Union

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup

ReplyMarkup = Union[ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, None]


@dataclass
class Answer:
    text: str
    reply_markup: ReplyMarkup = None
