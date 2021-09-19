from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    phone_number = State()
    email = State()
    biography = State()
    works = State()
    subjects = State()
    nickname = State()
