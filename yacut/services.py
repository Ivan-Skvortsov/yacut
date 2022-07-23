import string
import random

from yacut.models import URL_map


def short_id_exists_in_db(short_id):
    """Checks if given short_id already extists in database."""
    return URL_map.query.filter_by(short=short_id).first() is not None


def get_unique_short_id():
    """Random unique string generator with digits and letters."""
    while True:
        id = ''.join(random.choices(string.digits + string.ascii_letters, k=6))
        if not short_id_exists_in_db(id):
            return id
