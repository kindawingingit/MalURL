from flask import Flask, render_template
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from models.utils import _convert

app = Flask(__name__)


@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"
