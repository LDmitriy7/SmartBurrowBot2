from aiogram.dispatcher.filters.state import State, StatesGroup


class Withdraw(StatesGroup):
    amount = State()


class Deposit(StatesGroup):
    amount = State()
