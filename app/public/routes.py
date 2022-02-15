from flask import render_template

from . import public


@public.route('/')
def index():  # put application's code here
    return render_template('index.html')

