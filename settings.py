import os
import re
import string

ALLOWED_SIMBOLS = string.ascii_letters + string.digits
ALLOWED_SIMBOLS_API_SHORT = '^[a-zA-Z0-9]+$'
MAIN_URL = 'http://127.0.0.1:5000/'
SHORT_LINK_LENGTH = 6
SHORT_URL_PATTERN = '^[' + re.escape(ALLOWED_SIMBOLS) + ']+$'
INVALID_SHORT_URL = 'You can only use numbers and English letters.'
INDEX_URL = '/'
ORIGINAL_URL_PATTERN = (
    '^((ftp|http|https):\/\/)?(www\.)?([A-Za-zА-Яа-я0-9]{1}[A-Za-zА-Яа-я0-9\-]'
    '*\.?)*\.{1}[A-Za-zА-Яа-я0-9-]{2,8}(\/([\w#!:.?+=&%@!\-\/])*)?$'
)
INVALID_ORIGINAL_URL = (
    'You can only use address as http://ya.ru or https://ya.ru')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default='MY SECRET KEY is most secure')
