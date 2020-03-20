import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # gets the SECRET_KEY from an environment variable or defaults to string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # this stops Flask from signalling DB changes
