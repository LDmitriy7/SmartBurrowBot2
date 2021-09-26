import states
from .balance import *
from .create_order import *
from .registration import *

answers_for_states = {
    states.CreateOrder.work_type: ask_work_type,
    states.CreateOrder.subject: ask_subject,
    states.CreateOrder.until_date: ask_until_date,
    states.CreateOrder.description: ask_description,
    states.CreateOrder.price: ask_price,
    states.CreateOrder.note: ask_note,
    states.CreateOrder.files: ask_files,
    states.CreateOrder.preview: show_preview,

    states.Registration.phone_number: ask_phone_number,
    states.Registration.email: ask_email,
    states.Registration.biography: ask_biography,
    states.Registration.works: ask_works,
    states.Registration.subjects: ask_subjects,
    states.Registration.nickname: ask_nickname,

    states.Deposit.amount: ask_deposit_amount,

    states.Withdrawal.amount: ask_withdrawal_amount,
    states.Withdrawal.card_num: ask_withdrawal_card_num,
    states.Withdrawal.confirmation: ask_withdrawal_confirmation,
}
