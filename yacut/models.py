from datetime import datetime

from flask import url_for

from yacut import db


class URL_map(db.Model):
    """Model for URL mapping."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(6), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def serialize(self, show_short=False):
        """Serializes URL_map object to dictionary."""
        out = dict(url=self.original)
        if show_short:
            link = url_for(
                'redirect_view', custom_id=self.short, _external=True
            )
            out.update(dict(short_link=link))
        return out

    def deserialize(self, data):
        """Deserializes dictionary into URL_map object."""
        field_map = {
            'url': 'original',
            'custom_id': 'short'
        }
        for field in field_map:
            if field in data:
                setattr(self, field_map[field], data[field])
