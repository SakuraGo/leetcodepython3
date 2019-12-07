import time

def decorator(func):
    def wrapper(*args):  #使用可变参数.
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(func_name):
    print("This is a function named:"+func_name)

@decorator
def f2(func_name,funcname2):
    print("This is a function named:"+func_name +"~~"+funcname2)


f1('test func')
f2('test func','qwer')