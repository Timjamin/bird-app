from random import choice
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

app.secret_key = '********'

birds = [
    {"name": "Sparrow", "fact": "Sparrows are small birds that often live near people."},
    {"name": "Pigeon", "fact": "Pigeons can use the Earth's magnetic field to help navigate."},
    {"name": "Owl", "fact": "Many owls can turn their heads far around to look behind them."},
    {"name": "Penguin", "fact": "Penguins use their flipper-like wings to swim underwater."},
    {"name": "Eagle", "fact": "Eagles have excellent eyesight for spotting prey from far away."},
    {"name": "Robin", "fact": "Robins often find worms by watching the ground closely."},
    {"name": "Hummingbird", "fact": "Hummingbirds can hover in place while drinking nectar."},
    {"name": "Flamingo", "fact": "Flamingos get much of their pink coloring from their food."},
    {"name": "Peacock", "fact": "A peacock's colorful tail feathers are used in courtship displays."},
    {"name": "Woodpecker", "fact": "Woodpeckers use their strong bills to find insects in wood."},
    {"name": "Albatross", "fact": "Albatrosses can glide over the ocean for long distances."},
    {"name": "Kingfisher", "fact": "Kingfishers dive into water to catch fish."},
    {"name": "Ostrich", "fact": "Ostriches are large, flightless birds that can run quickly."},
    {"name": "Crow", "fact": "Crows can recognize human faces."},
    {"name": "Swan", "fact": "Swans have long necks that help them reach plants in the water."},
    {"name": "Toucan", "fact": "A toucan's large bill is lightweight despite its size."},
    {"name": "Kestrel", "fact": "Kestrels can hover while looking for small prey."},
    {"name": "Puffin", "fact": "Puffins use their colorful bills to carry several small fish at once."},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/birds")
def birdPage():
    return render_template("bird.html")

@app.route("/bird-types")
def birdTypesPage():
    return render_template("birdTypes.html")

@app.route("/not-birds")
def notBirdsPage():
    return render_template("notBirds.html")

@app.route("/random-bird")
def randomBirdPage():
    bird = choice(birds)
    return render_template("randomBird.html", bird=bird)

@app.route("/seasons")
def seasonPage():
    current_month = datetime.now().strftime("%B")
    current_year = datetime.now().year

    return render_template("seasons.html", month=current_month, year=current_year)

@app.route("/profile", methods=["GET", "POST"])
def profilePage():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        quan = request.form.get('quan', '').strip()
        comments = request.form.get('comments', '').strip()
        rel = request.form.get('rel', '').strip()
        accomodations = request.form.get('accomodations') == 'yes'

        if not name or not email or not quan or not rel:
            error = 'you did NOT fill out everything, are you STUPID?'
            return render_template('profileForm.html', error=error)

        return render_template('profileSuccess.html', name=name, email=email, quan=quan, rel=rel, comments=comments, accomodations=accomodations)

    return render_template('profileForm.html')
