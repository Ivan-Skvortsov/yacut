from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Оригинальная длинная сслыка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(6 ,6), Optional()]
    )
    submit = SubmitField('Создать')
