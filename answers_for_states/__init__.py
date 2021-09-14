import states
from .create_order import *

answers_for_states = {
    states.CreateOrder.work_type: ask_work_type,
    states.CreateOrder.subject: ask_subject,
    states.CreateOrder.date: ask_date,
    states.CreateOrder.description: ask_description,
    states.CreateOrder.price: ask_price,
    states.CreateOrder.note: ask_note,
}
