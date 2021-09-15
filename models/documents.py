from __future__ import annotations

from datetime import datetime

import mongoengine as me

import config
from . import constants


class Profile(me.EmbeddedDocument):
    nickname: str = me.StringField()
    phone_number: str = me.StringField()
    email: str = me.StringField()
    biography: str = me.StringField()
    deals_amount: int = me.IntField(default=0)
    works: list[str] = me.ListField(me.StringField())


class User(me.Document):
    user_id: int = me.IntField()

    balance: int = me.IntField(default=0)
    subjects: list[str] = me.ListField(me.StringField())
    profile: Profile = me.EmbeddedDocumentField(Profile)
    page_url: str = me.StringField()
    card_num: str = me.StringField()
    broadcast_allowed: bool = me.BooleanField(default=False)
    invited_by: int = me.IntField()
    reg_date: datetime = me.DateTimeField(default=datetime.now)

    ref_income: int = me.IntField(default=0)
    ref_percent: int = me.IntField(default=config.RefProgram.PERCENT)
    ref_term: int = me.IntField(default=config.RefProgram.TERM)


class File(me.EmbeddedDocument):
    file_type: str = me.StringField()
    file_id: str = me.StringField()


class Order(me.Document):
    status: str = me.StringField(default=constants.OrderStatus.ACTIVE)

    send_to: str = me.StringField()
    worker_id: int = me.IntField()
    require_approving: bool = me.BooleanField(default=False)

    work_type: str = me.StringField()
    subject: str = me.StringField()
    until_date: str = me.StringField()  # can't be date due to unknown error
    description: str = me.StringField()
    price: int = me.IntField()
    note: str = me.StringField()
    files: list[File] = me.EmbeddedDocumentListField(File)
