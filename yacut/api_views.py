import re
from http import HTTPStatus

from flask import jsonify, request

from settings import ALLOWED_SIMBOLS_API_SHORT, SHORT_LINK_LENGTH
from yacut import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_original_url(short):
    url_map = URLMap.get_short(short)
    if url_map:
        return jsonify(url_map.original, HTTPStatus.OK)
    raise InvalidAPIUsage(f'Указанная короткая ссылка: {short} - не найдена',
                          HTTPStatus.NOT_FOUND)


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('В запросе отсутствуют обязательные поля')
    elif 'url' not in data or 'custom_id' not in data:
        raise InvalidAPIUsage('Поле "url" и "custom_id" является обязательным')
    short = data.get('custom_id')
    if (
            not re.search(ALLOWED_SIMBOLS_API_SHORT, short) or
            len(short) > SHORT_LINK_LENGTH
    ):
        raise InvalidAPIUsage(
            'Недопустимое имя: используйте буквы латиницы и цифры')
    if URLMap.get_short(short):
        raise InvalidAPIUsage(
            f'Короткая ссылка {short} уже существует, попробуйте другую',
            HTTPStatus.BAD_REQUEST
        )
    if short is None:
        short = URLMap.get_unique_short_id()
    short_link = URLMap.create_short_link(short)
    url_map = URLMap(
        original=data.get('url'),
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
