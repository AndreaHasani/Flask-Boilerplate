from flask import Flask, render_template, request

import os

application = Flask(__name__)
APP_DIR = os.path.dirname(os.path.realpath(__file__))
application.config.from_pyfile('config.py')

from app.views import *
