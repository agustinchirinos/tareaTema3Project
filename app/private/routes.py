from flask import render_template

from . import private



@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    return render_template("indexcliente.html")