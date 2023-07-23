from http import HTTPStatus

from flask import abort, redirect, render_template

from settings import INDEX_URL
from yacut import app, db
from .error_handlers import ShortLinkNotFound
from .form import URLForm
from .models import URLMap


@app.route(INDEX_URL, methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    short_link = URLMap.create_short_link(custom_id)
    if not custom_id or custom_id == '':
        custom_id = URLMap.get_unique_short_id()
        short_link = URLMap.create_short_link(custom_id)
    url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(url)
    db.session.commit()
    return render_template(
        'index.html',
        short_link=short_link,
        form=form
    )


@app.route('/<short>')
def redirect_view(short):
    try:
        url = URLMap.query.filter_by(short=short).first_or_404()
        return redirect(url.original, code=HTTPStatus.FOUND)
    except ShortLinkNotFound:
        abort(HTTPStatus.NOT_FOUND)
