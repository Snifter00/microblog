from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
# this is located at the bottom to avoid circular dependencies
