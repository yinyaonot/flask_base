from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/login/')
def login():
    return '登录'

@users.route('/register/')
def register():
    return '注册'

