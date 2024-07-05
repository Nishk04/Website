from flask import Blueprint, render_template, request, redirect, url_for, session
# This file carries all the routes so it doesn't clutter the main file

# Use name of file: view
views = Blueprint(__name__, "views")

ap_classes = ['AP Calculus AB', 'AP Calculus BC', 'AP Physics 1', 'AP Phyiscs C']


@views.route("/")
def home():
    return render_template("base.html")

@views.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        # Session is a dictionary that a ton of information stored for an active session on server side
        session["user"] = user
        return redirect(url_for("views.user"))
    else:
        return render_template("login.html")

@views.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@views.route("/apselection", methods=['GET', 'POST'])
def apselection():
    selected_class = None
    if request.method == 'POST':
        selected_class = request.form.get('class')
        return redirect(url_for("study", cls=selected_class))
    else:
        return render_template("APSelection.html", ap_classes=ap_classes, selected_class=selected_class)

@views.route("/study<cls>")
def study(cls):
    return render_template("Study.html", cls=cls)

@views.route("/resources")
def resources():
    return None