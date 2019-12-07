def f1():
    a = 10
    def f2():
        a = 20 # a被python认为是一个局部变量，没有引用环境变量.
        ## 这里要引用一下函数外部的环境变量，又不要直接改变它。。。
        return a
    return f2

f = f1()
print(f) #<function f1.<locals>.f2 at 0x00000170A2FA7048>
print(f.__closure__)  #None

def f3():
    b = 50
    def f4():
        c = 5
        d = b*2
        print("qwer")
        return b**2
    return f4  # 这里不能是f4()， f4()会返回执行结果，而不是返回闭包...

ff =f3()
print(ff)
print(ff.__closure__)
print(ff.__closure__[0].cell_contents) #50 b==50

