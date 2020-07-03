from flask import Bluerprint

bp = Bluerprint('main', __name__)

from app.main import routes
