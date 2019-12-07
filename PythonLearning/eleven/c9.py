#一切皆对象

# 闭包

'''
函数
只是一段可执行的代码，并不是对象，(其他语言)

python
一切皆对象。结构

a = 1
a = '2'
a = def  #函数赋值给变量

int a = 1

函数当做另外一个函数的参数，

把函数当做另一个 函数的返回结果
'''
def a (x,y):
    return x*y


print(type(a)) # <class 'function'>
def demo(aaa,xx,yy):
    return aaa(xx,yy)
print(demo(a,3,5))

