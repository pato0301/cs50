from flask import Flask, jsonify, redirect, render_template, request
import cs50
import csv

# Configure application
app = Flask(__name__)
app.run(debug=True)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv", "r") as file:
        reader = csv.DictReader(file)
        surveys = list(reader)
    return render_template("sheet.html", surveys=surveys)


@app.route('/form', methods=["POST"])
def post_form():
    if not request.form["firstName"] or not request.form["lastName"] or not request.form["email"] or not request.form["character"]:
        return render_template("error.html", message="TODO")  # firstName + " " + lastName + " " + email)
    else:
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        character = request.form["character"]
        gender = request.form["gender"]
        jedi = request.form["jedi"]
        with open("survey.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["First_Name", "Last_Name", "Email", "Character", "Gender", "Type_Char"])
            writer.writerow({"First_Name": firstName, "Last_Name": lastName, "Email": email,
                             "Gender": gender, "Type_Char": jedi, "Character": character})
        return redirect("/sheet")