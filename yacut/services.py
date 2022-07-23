import string
import random

from yacut.models import URL_map


def get_unique_short_id():
    """Random unique string generator with digits and letters."""
    while True:
        id = ''.join(random.choices(string.digits + string.ascii_letters, k=6))
        if URL_map.query.filter_by(short=id).first() is None:
            return id
