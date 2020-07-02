from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
# this is located at the bottom to avoid circular dependencies
