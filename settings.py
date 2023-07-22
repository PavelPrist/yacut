import os
import re
import string

ALLOWED_SIMBOLS = string.ascii_letters + string.digits
ALLOWED_SIMBOLS_API_SHORT = '^[a-zA-Z0-9]+$'
MAIN_URL = 'http://localhost/'
SHORT_LINK_LENGTH = 6
SHORT_URL_PATTERN = '^[' + re.escape(ALLOWED_SIMBOLS) + ']+$'
INVALID_SHORT_URL = 'Указано недопустимое имя для короткой ссылки'
INDEX_URL = '/'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default='MY SECRET KEY is most secure')
