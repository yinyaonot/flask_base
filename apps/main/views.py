from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/main/')
def homepage():
    return '主页'
