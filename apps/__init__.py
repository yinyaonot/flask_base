from flask import Flask

from apps.user.views import user


def create_app():
    app = Flask(__name__)
    app.debug = True
    blue_register(app)
    return app

def blue_register(app):
    app.register_blueprint(user)
    return app