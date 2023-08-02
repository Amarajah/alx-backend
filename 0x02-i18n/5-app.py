#!/usr/bin/env python3
""" basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Get the list of supported languages from the app's config
    Extract the user's preferred languages from the
    request's Accept-Language header
    The `best_match` method returns the best-matching language
    code from the supported_languages list"""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """returns a user dictionary or None if the ID cannot be found """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """before_request should use get_user to find a user if any,
    and set it as a global on flask.g.user."""
    user = get.user()
    g.user = user


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
