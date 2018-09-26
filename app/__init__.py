from flask import Flask

from config import config_by_name
from app.v1.app import orders


def create_app(self):
    app = Flask(__name__)
    return app
