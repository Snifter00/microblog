from app import db


class User(db.Model):
    """Inherits db.Model from Flask-SQLAlchemy, where it is
    a base class for all models. The following code defines
    the database schema."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # __tablename__= string to overide default table name, 'user'

    def __repr__(self):
        """This tells python how to print object of this class"""
        return '<User {}.'.format(self.username)
