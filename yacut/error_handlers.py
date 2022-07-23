from flask import jsonify, render_template

from yacut import app, db


class APIExceptionHandler(Exception):
    """Handler for API exceptions."""
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def serialize(self):
        return dict(message=self.message)


@app.errorhandler(APIExceptionHandler)
def invalid_api_usage(error):
    return jsonify(error.serialize()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
