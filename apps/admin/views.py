from flask import Blueprint

administor = Blueprint('administor', __name__)


@administor.route('/alogin/')
def admin_login():
    return '管理员'
