import os


class Config(object):
    # gets the SECRET_KEY from an environment variable or defaults to string
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
