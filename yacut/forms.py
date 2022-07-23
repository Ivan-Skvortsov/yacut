from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import (DataRequired, Length, Optional, Regexp,
                                URL, ValidationError)

from yacut.services import short_id_exists_in_db


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Оригинальная длинная сслыка',
        validators=[
            DataRequired(message='Это поле обязательно для заполнения'),
            URL(message='Введите корректный URL')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                1, 16, message='Ссылка должна быть длиной от 1 до 16 символов'
            ),
            Regexp(
                r'^[a-zA-Z0-9]+$',
                message='Ссылка должна состоять из цифр и латинских букв'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(form, field):
        """Validates if given custom_id unique."""
        if short_id_exists_in_db(field.data):
            raise ValidationError(
                f'Имя {field.data} уже занято! Выберите, пожалуйста, другое!'
            )
