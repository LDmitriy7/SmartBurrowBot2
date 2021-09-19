import toml

try:  # TODO
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
    OWNER_URL = users['owner_url']


class Log:
    log = env['Log']

    FILE = log.get('file')
    LEVEL = log.get('level', 30)


class ArticleUrls:
    article_urls = env['ArticleUrls']

    ABOUT_PROJECT = article_urls['about_project']
    PROJECT_RULES = article_urls['project_rules']
    CLIENT_MENU_GUIDE = article_urls['client_menu_guide']
    WORKER_MENU_GUIDE = article_urls['worker_menu_guide']
    FAQ = article_urls['faq']
