#!/usr/bin/env python3
""" Flask application """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ l18n Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object("1-app.Config")
babel = Babel(app)


@app.route("/")
def hello_world():
    """ Handle default route """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ Gets the best matching language for user """
    return request.accept_languages.best_match(Config.LANGUAGES)
