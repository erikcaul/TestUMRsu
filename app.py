import re
from flask import Flask, abort, redirect, render_template, request
from html import escape
from werkzeug.exceptions import default_exceptions, HTTPException

app = Flask(__name__)

@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    return render_template("index.html")

"""@app.route("/submit")
def result():
    return render_template("result.html")"""
    