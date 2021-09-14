from flask import Blueprint, g, redirect, render_template, request, session
from libposts import get_posts, post

mod_welcome = Blueprint("mod_welcome", __name__, template_folder="templates")


@mod_welcome.route("/")
def do_welcome():

    if "username" not in session:
        return redirect("/user/login")

    posts = get_posts(session["username"])

    return render_template("welcome.html", posts=posts)


@mod_welcome.route("post", methods=["POST"])
def do_post():

    if not session["username"]:
        return redirect("/user/login")

    if request.method == "POST":

        username = session["username"]
        text = request.form.get("text")

        post(username, text)

    return redirect("/")
