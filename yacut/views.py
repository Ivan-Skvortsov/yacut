from flask import Markup, render_template, flash, redirect, url_for

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URL_map
from yacut.services import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    url_map = URL_map(
        original=form.original_link.data,
        short=form.custom_id.data or get_unique_short_id()
    )
    db.session.add(url_map)
    db.session.commit()
    link = url_for(
        'redirect_view', custom_id=url_map.short, _external=True
    )
    message = Markup(
        f'Ваша новая сслыка готова: <a href="{link}">{link}</a>'
    )
    flash(message)
    return render_template('index.html', form=form)


@app.route('/<string:custom_id>', methods=['GET'])
def redirect_view(custom_id):
    url_map = URL_map.query.filter_by(short=custom_id).first_or_404()
    return redirect(url_map.original)
