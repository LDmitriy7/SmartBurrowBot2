from datetime import date


def format_date(date_: date) -> str:
    parts = str(date_).split('-')
    return '-'.join(reversed(parts))
