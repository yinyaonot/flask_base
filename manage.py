from flask import Flask
from flask import render_template
from flask_script import Manager, Server

# from console.console01 import create_apps
from urls import create_app, test

app = create_app()
'''
第一步 导入Manager对象
第二步 实例化
'''
manager = Manager(app=app)
manager.add_command('start', Server(port=6000, use_debugger=True))


# 控制层
# 路由系统 配置首页
@test.route('/login/')
def login():
    return render_template('login.html')
    # return 'hello'


if __name__ == '__main__':
    manager.run()
