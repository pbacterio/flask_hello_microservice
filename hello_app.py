#!/usr/bin/env python3

from os import environ
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello {}".format(environ['NAME'])