from flask_script import Manager, Server

from apps import create_app

app = create_app()
'''
第一步 导入Manager对象
第二步 实例化
'''
manager = Manager(app=app)
manager.add_command('start', Server(port=6000))

if __name__ == '__main__':
    manager.run()
