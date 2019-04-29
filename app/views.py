from flask import Flask, render_template, request, session, jsonify, abort
from app.models import *
from app import application
from app.functions import *


@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")
