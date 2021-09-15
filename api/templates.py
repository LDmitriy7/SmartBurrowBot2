import models
from models import constants
from texts import templates


def get_order_post_text(order: models.Order, with_note=False) -> str:
    from api.dates import format_date_short

    statuses = {
        constants.OrderStatus.ACTIVE: '🔥 Активен',
        constants.OrderStatus.IN_PROGRESS: '⏳ Выполняется',
        constants.OrderStatus.COMPLETED: '✅ Выполнен',
    }

    return templates.order_post.format(
        status=statuses[order.status],
        work_type=order.work_type.replace(' ', '_'),
        subject=order.subject.replace(' ', '_'),
        description=order.description,
        price=f'{order.price} грн' if order.price else 'Договорная',
        until_date=format_date_short(order.until_date),
        note=f'<b>Твоя заметка:</b> {order.note}' if order.note and with_note else '',
    )
