from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/birds")
def birdPage():
    return render_template("bird.html")

@app.route("/seasons")
def seasonPage():
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year

    return render_template("season.html", month=current_month, year=current_year)