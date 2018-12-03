from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/login/')
def login():
    return '登录'

@user.route('/register/')
def register():
    return '注册'

