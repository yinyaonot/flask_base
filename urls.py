from flask import Flask, Blueprint

test = Blueprint('test', __name__)


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(test, url_prefix='/test')
