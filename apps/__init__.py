from flask import Flask

from apps.admin.views import administor
from apps.detail.views import detail
from apps.main.views import main
from apps.user.views import users


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.register_blueprint(administor)
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(detail)
    # blue_register(app)
    return app


def blue_register(app):
    app.register_blueprint(administor)
    app.register_blueprint(user)
    app.register_blueprint(main)
    app.register_blueprint(detail)

