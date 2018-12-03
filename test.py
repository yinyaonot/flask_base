class User:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def show(self):
        print(self.name,self.age,self.sex)


import datetime
import decimal
from collections import Iterable


def obj_to_dict(obj):
    result = {}
    if obj:
        # 将对象所有属性值,转化成字典形式
        keys = vars(obj).keys()
        if keys:
            for key in keys:
                if not key.startswith('_'):
                    value = getattr(obj, key)
                    if isinstance(value, datetime.datetime):
                        value = value.strftime('%Y-%m-%d %H:%i:%s ')
                    elif isinstance(value, datetime.date):
                        value = value.strftime('%Y-%m-%d')
                    elif isinstance(value, decimal.Decimal):
                        value = float(value)
                    result[key] = value
    return result

# 将QuerySet对象转化列表套字典
def to_list(objects):
    li = []
    if objects and isinstance(objects, Iterable):
        for obj in objects:
            li.append(obj_to_dict(obj))
    return li



if __name__ == '__main__':
    user = User('nihao',18,'nan')
    dic = obj_to_dict(user)
    print(dic)