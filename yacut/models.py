import random
from datetime import datetime

from flask import url_for

from settings import ALLOWED_SIMBOLS, MAIN_URL, SHORT_LINK_LENGTH
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String)
    short = db.Column(
        db.String(SHORT_LINK_LENGTH), unique=True, nullable=False
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short=self.short, _external=True
            )
        )

    @staticmethod
    def get_short(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_unique_short_id():
        while True:
            short = ''.join(
                random.choices(ALLOWED_SIMBOLS, k=SHORT_LINK_LENGTH)
            )
            if not URLMap.get_short(short):
                break
        return short

    @staticmethod
    def create_short_link(short_generated):
        if short_generated:
            short_link = MAIN_URL + short_generated
            return short_link
        return None