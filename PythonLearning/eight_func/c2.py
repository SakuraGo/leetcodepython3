import sys
# sys.setrecursionlimit(10000) ##最大递归层数

def add(x,y):
    return x+y

def print_code(code):##避免与内置函数同名
    print(code)

a = add(1,2)
b = print_code("qwer")
print_code("qwer")
print(a,b)

def test():
    for i in range(10):
        if i == 7:
            return
        else:
            print_code(i)

test()

def ddd(x,y):
    return x*2+10,y*3+5

sk1,sk2  = ddd(23,55)
print(sk1,sk2)