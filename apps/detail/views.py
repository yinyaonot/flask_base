from flask import Blueprint

detail = Blueprint('detail', __name__)


@detail.route('/detailinfo/')
def detail_info():
    return '详情'
