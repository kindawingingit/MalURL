from flask import Flask, render_template
from convert import _convert

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"
