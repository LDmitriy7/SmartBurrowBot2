import toml

_config = toml.load('.config.toml')

TELEGRAM_BASE_URL = 'https://t.me/'


class Database:
    _data = _config['Database']

    NAME = _data['name']
    HOST = _data.get('host', 'localhost')
    PORT = _data.get('port', 27017)
    USERNAME = _data.get('username')
    PASSWORD = _data.get('password')
    AUTH_SOURCE = _data.get('auth_source', 'admin')


class Bot:
    _data = _config['Bot']

    TOKEN = _data['token']
    SKIP_UPDATES = _data.get('skip_updates', False)


class BrokerBot:
    _data = _config['BrokerBot']

    TOKEN = _data['token']


class Users:
    _data = _config['Users']

    ADMINS_IDS = _data['admins_ids']
    DEVELOPERS_IDS = _data['developers_ids']
    OWNER_ID = _data['owner_id']
    OWNER_USERNAME: str = _data['owner_username']
    OWNER_URL = OWNER_USERNAME.replace('@', TELEGRAM_BASE_URL)


class Log:
    _data = _config['Log']

    FILE = _data.get('file')
    LEVEL = _data.get('level')


class ArticleUrls:
    ABOUT_PROJECT = 'https://telegra.ph/O-proekte-03-17'
    PROJECT_RULES = 'https://telegra.ph/Pravila-proekta-09-14'
    CLIENT_MENU_GUIDE = 'https://telegra.ph/Kak-ispolzovat-Menyu-zakazchika-03-17'
    WORKER_MENU_GUIDE = 'https://telegra.ph/Kak-ispolzovat-Menyu-ispolnitelya-03-17'
    FAQ = 'https://telegra.ph/CHasto-zadavaemye-voprosy-03-17'


class Channel:
    _data = _config['Channel']

    USERNAME = _data['username']
    URL = USERNAME.replace('@', TELEGRAM_BASE_URL)
    POST_URL = URL + '/{}'


class Merchant:
    _data = _config['Merchant']

    ID = _data['id']
    SECRET_KEY = _data['secret_key']


class RefProgram:
    PERCENT = 20
    TERM = 365 * 24 * 60 * 60


class Order:
    MIN_DESCRIPTION_LEN = 15
    MAX_DESCRIPTION_LEN = 500
