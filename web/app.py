import sys

from flask import Flask, render_template, request

sys.path.append("..")
from models.utils import _predict

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        name = request.form["url"]
        results = _predict(name)
        return render_template("predict.html", prediction=results)
        
