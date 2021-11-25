#!/usr/bin/env python3
""" Flask application """


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """ Handle default route """
    return render_template("0-index.html")
