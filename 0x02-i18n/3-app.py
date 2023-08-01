#!/usr/bin/env python3
""" basic Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Config class to hold the available babel languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles route
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Get the list of supported languages from the app's config
    Extract the user's preferred languages from the
    request's Accept-Language header
    The `best_match` method returns the best-matching language
    code from the supported_languages list"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
