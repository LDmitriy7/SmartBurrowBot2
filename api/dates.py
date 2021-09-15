def format_date(iso_date: str) -> str:
    parts = iso_date.split('-')
    return '-'.join(reversed(parts))


def format_date_short(iso_date: str) -> str:
    parts = iso_date.split('-')[1:]
    return '.'.join(reversed(parts))
