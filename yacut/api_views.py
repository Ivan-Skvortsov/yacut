import re

from flask import jsonify, request

from yacut import app, db
from yacut.models import URL_map
from yacut.error_handlers import APIExceptionHandler
from yacut.services import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    validate_api_input(data)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    url_map = URL_map()
    url_map.deserialize(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.serialize(show_short=True)), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URL_map.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify(url.serialize()), 200
    raise APIExceptionHandler('Указанный id не найден', 404)


def validate_api_input(data):
    if data is None:
        raise APIExceptionHandler('Отсутствует тело запроса', 400)
    if 'url' not in data:
        raise APIExceptionHandler('\"url\" является обязательным полем!', 400)
    if not re.match(r'^https?://', data['url']):
        raise APIExceptionHandler('Указан недопустимый url!', 400)

    custom_id = data.get('custom_id')
    if not custom_id:
        return
    if not 1 < len(custom_id) < 16:
        raise APIExceptionHandler('Указано недопустимое имя для короткой ссылки', 400)
    if not re.match(r'^[a-zA-Z0-9]+$', custom_id):
        raise APIExceptionHandler('Указано недопустимое имя для короткой ссылки', 400)
    if URL_map.query.filter_by(short=custom_id).first() is not None:
        raise APIExceptionHandler(f'Имя "{custom_id}" уже занято.', 400)
