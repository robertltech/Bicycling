from flask import render_template, abort, request
from html import escape
from SurveyViews import app
import csv

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")

@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
    return render_template("error.html", message="TODO")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    return render_template("error.html", message="TODO")

@app.route("/sheet2", methods=["POST"])
def post_sheet2():
    if not request.form.get("name") or not request.form.get("rang"):
        abort(400, "missing name")
    elif request.form.get("name").isalpha() and request.form.get("rang").isdigit():
        with open('survey.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([request.form.get("name"), request.form.get("rang")])           
    else:
        abort(400, "non-alpha name or server error")

    with open('survey.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            return render_template("sheet2.html", reader=reader)

            