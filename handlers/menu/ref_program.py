from aiogram import types
from aiogram.utils.deep_linking import get_start_link

import keyboards as kb
import models
import texts
from loader import dp


@dp.message_handler(text=kb.MainMenu.REF_PROGRAM)
async def send_ref_program_info(msg: types.Message):
    user = models.User.objects(user_id=msg.from_user.id).first()
    refs = [u for u in models.User.objects() if u.invited_by == msg.from_user.id]
    ref_link = await get_start_link(f'ref-{msg.from_user.id}')

    await msg.answer(
        texts.ref_program_info.format(ref_link=ref_link, refs_count=len(refs), ref_income=user.ref_income),
        disable_web_page_preview=True,
    )
