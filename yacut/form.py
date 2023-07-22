from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import InputRequired, Length, Optional, Regexp, \
    ValidationError

from settings import INVALID_ORIGINAL_URL, INVALID_SHORT_URL, \
    ORIGINAL_URL_PATTERN, \
    SHORT_LINK_LENGTH, SHORT_URL_PATTERN
from yacut.models import URLMap

ORIGINAL_URL_COMMENT = 'Добавьте вашу оригинальную ссылку https://.....'
SHORT_URL_COMMENT = (
    'Добавьте короткую ссылку или она будет добавлена автоматически')
REQUIRED_URL = 'Это поле обязательно для заполнения'
SUBMIT_COMMENT = 'Создать короткую ссылку'
SHORT_LINK_IS = 'Короткая ссылка {short} уже существует, попробуйте другую'


class URLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_URL_COMMENT,
        validators=[
            InputRequired(
                message=REQUIRED_URL
            ),
            Regexp(
                regex=ORIGINAL_URL_PATTERN,
                message=INVALID_ORIGINAL_URL
            )
        ]
    )
    custom_id = URLField(
        SHORT_URL_COMMENT,
        validators=[
            Length(
                max=SHORT_LINK_LENGTH,
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
