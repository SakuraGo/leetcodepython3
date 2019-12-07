import time

def decorator(func):
    def wrapper(*args,**kw):  #使用可变参数.
        print(time.time())
        func(*args,**kw)  ##可以调用任何多种类的参数
    return wrapper

@decorator
def f1(func_name):
    print("This is a function named:"+func_name)

@decorator
def f2(func_name,funcname2):
    print("This is a function named:"+func_name +"~~"+funcname2)

@decorator
def f3(func_name,funcname2,**kw):
    print("This is  a func named:"+func_name+funcname2)
    print(kw)

f1('test func')
f2('test func','qwer')
f3("qwer","asdf",a=1,b=2,c="123")
