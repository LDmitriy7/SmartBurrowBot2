import toml

try:
    env = toml.load('env.toml')
except:
    env = toml.load('../env.toml')


class Database:
    db = env['Database']

    NAME = db['name']
    HOST = db.get('host', 'localhost')
    PORT = db.get('port', 27017)
    USERNAME = db.get('username')
    PASSWORD = db.get('password')
    AUTH_SOURCE = db.get('auth_source', 'admin')


class Bot:
    bot = env['Bot']

    TOKEN = bot['token']
    SKIP_UPDATES = bot.get('skip_updates', False)


class Users:
    users = env['Users']

    ADMINS_IDS = users['admins_ids']
    OWNER_USERNAME = users['owner_username']


class Log:
    log = env['Log']

    FILE = log.get('file')
    LEVEL = log.get('level', 30)
