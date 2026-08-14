from flask import Flask, render_template, request, redirect, url_for

from database import(
    create_table,
    add_student,
    get_all_students,
    delete_student,
    update_student,
    search_student
)

app = Flask(__name__)

create_table()

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        student_id = request.form["student_id"]
        username = request.form["username"]
        semester = request.form["semester"]

        add_student(
            student_id,
            username,
            semester
        )
        return "Student Added Successffully"
    
    return render_template("form.html")

@app.route("/view")
def view_students():

    students = get_all_students()

    count = len(students)

    return render_template("view.html",
                           students=students,
                           count=count)

@app.route("/delete/<student_id>")
def delete(student_id):

    delete_student(student_id)
    return redirect(url_for("view_students"))

@app.route("/update", methods = ["GET", "POST"])
def update():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        semester = request.form["semester"]

        update_student(
            student_id,
            name,
            semester
        )
        return "student Updated"
    return render_template("update.html")

@app.route("/update/<student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    if request.method == "POST":

        name = request.form["name"]
        semester = request.form["semester"]

        update_student(
            student_id,
            name,
            semester
        )
        return redirect(url_for("view_students"))

    student = search_student(student_id)

    return render_template("edit_student.html",
                           student=student)

@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":

        student_id = request.form["student_id"]

        student = search_student(student_id)

        return render_template("search_result.html", student=student)

    return render_template("search.html")

app.run(debug=True)