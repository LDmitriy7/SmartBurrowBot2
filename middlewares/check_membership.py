from typing import Union

from aiogram import types, Bot
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import BadRequest


class CheckMembership(BaseMiddleware):
    """Check if user is member of group or subscribed on channel."""

    def __init__(self, chat_id: Union[str, int], error_text: str):
        self.chat_id = chat_id
        self.error_text = error_text
        super().__init__()

    async def is_chat_member(self, user_id: int) -> bool:
        """Check if user is currently member of chat."""
        bot = Bot.get_current()
        try:
            chat_member = await bot.get_chat_member(self.chat_id, user_id)
            return chat_member.is_chat_member()
        except BadRequest:
            return False

    async def on_pre_process_message(self, msg: types.Message, *_args):
        is_chat_member = await self.is_chat_member(msg.from_user.id)
        if not is_chat_member:
            await msg.answer(self.error_text)
            raise CancelHandler

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, *_args):
        is_chat_member = await self.is_chat_member(query.from_user.id)
        if not is_chat_member:
            await query.answer(self.error_text, show_alert=True)
            raise CancelHandler
