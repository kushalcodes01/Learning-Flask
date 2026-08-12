from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    semester = 5

    return render_template("home.html", semester = semester)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

app.run(debug=True)