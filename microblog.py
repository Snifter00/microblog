# This element defines the Flask application instance
from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

# Creates a shell context annd adds the database instance and models to the session
# run 'flask shell' to invoke this function.

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
