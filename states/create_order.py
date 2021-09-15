from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateOrder(StatesGroup):
    work_type = State()
    subject = State()
    until_date = State()
    description = State()
    price = State()
    note = State()
    files = State()
    preview = State()
