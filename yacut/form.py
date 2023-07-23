from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (
    InputRequired, Length, Optional, Regexp, URL, ValidationError)

from settings import (
    INVALID_ORIGINAL_URL, INVALID_SHORT_URL,
    SHORT_LINK_LENGTH, SHORT_LINK_LENGTH_MAX, SHORT_URL_PATTERN
)
from yacut.models import URLMap

ORIGINAL_URL_COMMENT = 'Добавьте вашу http://,https://...оригинальную ссылку'
SHORT_URL_COMMENT = (
    'Добавьте короткую ссылку или она будет добавлена автоматически')
REQUIRED_URL = 'Это поле обязательно для заполнения'
SUBMIT_COMMENT = 'Создать короткую ссылку'
SHORT_LINK_IS = 'Имя {short} уже занято!'


class URLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_URL_COMMENT,
        validators=[
            InputRequired(
                message=REQUIRED_URL
            ),
            URL(message=INVALID_ORIGINAL_URL)
        ]
    )
    custom_id = URLField(
        SHORT_URL_COMMENT,
        validators=[
            Length(
                max=SHORT_LINK_LENGTH_MAX,
                message=INVALID_SHORT_URL
            ),
            Optional(),
            Regexp(
                regex=SHORT_URL_PATTERN,
                message=INVALID_SHORT_URL
            )
        ]
    )
    submit = SubmitField(
        SUBMIT_COMMENT
    )

    def validate_custom_id(form, field):
        if URLMap.get_short(field.data):
            raise ValidationError(
                SHORT_LINK_IS.format(
                    short=field.data
                )
            )
