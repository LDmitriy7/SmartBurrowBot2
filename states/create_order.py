from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateOrder(StatesGroup):
    work_type = State()
    subject = State()
    date = State()
    description = State()
    price = State()
    note = State()
    files = State()
    preview = State()
