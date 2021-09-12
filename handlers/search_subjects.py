from aiogram import types

import api
import states
from loader import dp


@dp.inline_handler(state=[states.CreateOrder.subject])
async def show_fit_subjects(query: types.InlineQuery):
    fit_subjects = api.get_fit_subjects(query.query, limit=20)
    articles = []

    for index, subject in enumerate(fit_subjects):
        imc = types.InputTextMessageContent(subject)
        article = types.InlineQueryResultArticle(
            id=str(index),
            title=subject,
            input_message_content=imc,
        )
        articles.append(article)

    await query.answer(articles)
