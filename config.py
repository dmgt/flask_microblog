import os

#  configuration settings defined as class variables inside the Config class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'