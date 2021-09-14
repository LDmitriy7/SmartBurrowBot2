import re

from aiogram import types


def check_on_contacts(msg: types.Message) -> bool:
    """Return True if there are contacts in message_text."""
    met = types.MessageEntityType
    lower_text = msg.text.lower()
    user = msg.from_user

    for e in msg.entities:
        if e.type in [met.MENTION, met.URL, met.EMAIL, met.PHONE_NUMBER, met.TEXT_LINK]:
            return True

    if user.username and user.username.lower() in lower_text:
        return True

    if re.search(r'[0-9-–(). ]{9,}', lower_text):
        return True

    return False
