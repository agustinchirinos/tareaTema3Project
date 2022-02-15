from flask import Blueprint
private = Blueprint('private', __name__, template_folder='templates', static_folder='static')

from . import routes