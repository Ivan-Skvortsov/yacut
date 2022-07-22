from datetime import datetime

from yacut import db


class URL_map(db.Model):
    """Model for URL mapping."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256))
    short = db.Column(db.String(6))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
