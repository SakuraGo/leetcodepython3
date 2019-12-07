#装饰器.

import time

def decorator(func):# 装饰.
    def wrapper(): # 被封装
        print(time.time())
        func()
    return wrapper

def f1():
    print("This is a function.11..")


def f2():
    print("This is a ffff22")

f = decorator(f1)
f()