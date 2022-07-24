import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', default='YHjk*(#KF9398HJklfhskdjf8~!@&*)')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
