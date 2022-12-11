from flask import Flask, render_template, request

from models import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_profile", methods=["POST"])
def create_profile():
    name = request.form.get("name")
    email = request.form.get("email")
    top_ten = request.form.get("top_ten")

    user = User(name=name, email=email, top_ten=top_ten)
    db.session.add(user)
    db.session.commit()

    return render_template("profile.html", user=user)


@app.route("/share_top_ten", methods=["POST"])
def share_top_ten():
    user_id = request.form.get("user_id")
    user = User.query.get(user_id)
    user.share_top_ten()

    return render_template("share.html", user=user)


if __name__ == "__main__":
    app.run()
