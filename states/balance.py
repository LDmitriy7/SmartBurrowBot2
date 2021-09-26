from aiogram.dispatcher.filters.state import State, StatesGroup


class Withdrawal(StatesGroup):
    amount = State()
    card_num = State()
    confirmation = State()


class Deposit(StatesGroup):
    amount = State()
