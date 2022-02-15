from flask import Flask, render_template, request



app = Flask(__name__)


from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return  app