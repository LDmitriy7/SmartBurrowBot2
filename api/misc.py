from typing import Optional, Callable, Awaitable

from answers_for_states import answers_for_states
from loader import dp

AsyncFunction = Callable[[], Awaitable]


async def get_answer_for_state() -> Optional[AsyncFunction]:
    cur_state = dp.current_state()
    cur_state = await cur_state.get_state()

    for state, answer in answers_for_states.items():
        if state.state == cur_state:
            return answer
    else:
        raise KeyError('There is no answer for this state.')


async def answer_for_state():
    answer = await get_answer_for_state()
    await answer()
