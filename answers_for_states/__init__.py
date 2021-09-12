import states
from .misc import *

answers_for_states = {
    states.CreateOrder.work_type: ask_work_type,
    states.CreateOrder.subject: ask_subject,
}
