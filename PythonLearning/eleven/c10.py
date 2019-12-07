#闭包

# a = 33
def curve_pre():
    a = 25
    def curve(x):
        return a*x**2  ## 若a是在模块级的变量，那么a改变的话 curve中的a也会改变
        print('This is a function....')
        pass
    return curve

# curve() # not defined

# 闭包 = 函数+环境变量
#若
a = 10  ##对curve中的a没有影响 , curve中的环境变量只有在定义的时候会,
#

f = curve_pre() #得到curve()函数

print(f(2))
print(f.__closure__) ##环境变量 , 若a是模块级别，这里是None
print(f.__closure__[0].cell_contents) ##第一个环境变量的值

