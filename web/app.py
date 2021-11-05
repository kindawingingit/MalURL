from flask import Flask, render_template, request
"""
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
"""

import sys
sys.path.append("..")
from models.utils import _predict

app = Flask(__name__)

_predict("www.google.com")

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"
	
@app.route("/predict")
def predict():
	name = request.form.values()
	print(name)
	print(type(name))
