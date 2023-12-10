from flask import Blueprint, render_template


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html", title="Главная")

@main.route("/blog")
def blog():
    return render_template("index.html", title="Blog")


@main.route("/html")
def html_page():
    return render_template("html_page.html")


@main.route("/django")
def django_page():
    return render_template("django_page.html")


@main.route("/css")
def css_page():
    return render_template("css_page.html")


@main.route("/python")
def python_page():
    return render_template("python_page.html")


@main.route("/js")
def js_page():
    return render_template("js_page.html")


@main.route("/flask")
def flask_page():
    return render_template("flask_page.html")
