from flask import redirect, render_template, request, url_for

from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        # Handle form submission
        pass
    else:
        # Render profile page
        pass


@app.route("/topten", methods=["GET", "POST"])
def topten():
    if request.method == "POST":
        # Handle form submission
        pass
    else:
        # Render top ten page
        pass


@app.route("/social", methods=["GET", "POST"])
def social():
    if request.method == "POST":
        # Handle form submission
        pass
    else:
        # Render social page
        pass
