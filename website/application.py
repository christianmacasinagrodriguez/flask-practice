from flask import Flask, render_template, request, Blueprint

application = Blueprint('app', __name__)

SPORTS = [
    "Chess",
    "Badminton",
    "Soccer",
    "Mobile Legends",
    "Dota 2"

]

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))

@application.route("/register")
def reg():
    return render_template("registration.html", sports=SPORTS)

@application.route("/submit")
def submit():
    name = request.args.get("applicant")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.args.get("laro")
    if not sport:
        return render_template("error.html", message="Please choose sports")
    sport = request.args.get("laro")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sports")
    return render_template("success.html")
