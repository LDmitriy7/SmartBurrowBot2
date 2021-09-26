from loader import dp
from .answer_any_query import AnswerAnyQuery
from .check_membership import CheckMembership
import config
import texts


def setup():
    dp.setup_middleware(AnswerAnyQuery())
    dp.setup_middleware(CheckMembership(config.Channel.USERNAME, texts.check_subscription_error))
