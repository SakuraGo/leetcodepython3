#装饰器.

import time

def decorator(func):# 装饰.
    def wrapper(): # 被封装
        print(time.time())
        func()
    return wrapper

@decorator  #给f1加了个装饰器..
def f1():
    print("This is a function.11..")


def f2():
    print("This is a ffff22")

f1()
# @
# f = decorator(f1)

