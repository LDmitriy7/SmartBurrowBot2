from __future__ import annotations

import models


def get_all_nicknames() -> set[str]:
    nicknames = set()

    for user in models.User.objects():
        user: models.User
        if user.profile:
            nicknames.add(user.profile.nickname)

    return nicknames
