order_post = """
<b>{status}</b>

#{work_type}
#{subject}

{description}

<b>Сдача:</b> {until_date}
<b>Цена:</b> {price}
{note}
"""

# _AVG_RATING_TEMPLATE = """\
# Качество: {quality_text} ({quality:.2f})
# Сроки: {terms_text} ({terms:.2f})
# Контактность: {contact_text} ({contact:.2f})\
# """
#
# _WORKER_BID_TEMPLATE = """
# [&#8203;]({post_url})
# Автор <a href="{worker_url}">{worker_nickname}</a> отклинкулся на ваш проект:
# *Средний рейтинг*:
# {avg_rating}
# {bid_text}
# """
#
# _CLIENT_BID_TEMPLATE = """
# Заказчик {client_name} предлагает вам персональный проект
# """
#
# _PROFILE_TEMPLATE = """
# Никнейм: {nickname}
# Телефон: {phone_number}
# Email: {email}
# Ссылка на личную страницу:
# {page_url}
# """
#
#
# def form_client_bid_text(client_name: str) -> str:
#     """Создает текст для заявки исполнителю от клиента."""
#     return _CLIENT_BID_TEMPLATE.format(**locals())
#
#
# def form_avg_rating_text(rating: dict) -> str:
#     """Создает текст со средним рейтингом по шаблону."""
#     text_rating = {f'{rate}_text': round(amount) * '⭐' for rate, amount in rating.items()}
#     return _AVG_RATING_TEMPLATE.format(**rating, **text_rating)
#
#
# def form_subjects_text(subjects: list) -> str:
#     """Создает список предметов (текст)."""
#     subjects = [f' • {s}' for s in subjects]
#     result = '\n'.join(subjects)
#     return result
#
#
# def form_worker_bid_text(worker_nickname: str, worker_url: str, post_url: str, avg_rating: str, bid_text: str) -> str:
#     if bid_text is None:
#         bid_text = ''
#     else:
#         bid_text = f'*Комментарий*:\n{bid_text}'
#
#     return _WORKER_BID_TEMPLATE.format(**locals())
#
#
# def form_profile_template(nickname: str, phone_number: str, email: str, page_url: str):
#     return _PROFILE_TEMPLATE.format(**locals())
