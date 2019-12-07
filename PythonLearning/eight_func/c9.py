##变量作用域

c = 50
def add(x,y):
    c = x + y
    print(c)

add(1,2)
print(c)


def demo():
    cc  = 10

demo()
# print(cc)   ##报错.NameError: name 'cc' is not defined

a  =[1,2,3]
b = [1,2,3]
print(id(a),id(b)) ### 1993128587144 1993130549512

def demo2():
    print(b)  ##可调用外部的b
demo2()

def demo3():
    c = 10

    #块级作用域  ##函数可以形成作用域，一个for循环无法形成作用域
    for i in range(0,9):
        a = "a"
        c += 1
    print(c)
    print(a)  ## 居然可以调用for循环里面的东西！

demo3()

