from flask import Blueprint, redirect, render_template

mod_hello = Blueprint("mod_hello", __name__, template_folder="templates")


@mod_hello.route("/")
def do_hello():
    return "hello :)"
