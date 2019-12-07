#装饰器

import time
def f1():
    # print(time.time())
    print("This is a function.11..")

f1()
#unix 时间戳

def f2():
    print("This is a ffff22")

#打印时间.
def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)


