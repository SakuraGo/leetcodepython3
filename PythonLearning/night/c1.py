## 面向对象
##
## 类与对象

##类最基本的作用，封装代码
class Student():
    ## 这里的是类变量
    ## 一个班级里所有学生的总数
    summ = 0
    name = "wang" ##类变量
    age  = 0

    def __init__(self,name,age): ##初始化函数/构造函数
        ## 实例化时候，自动调用，
        ## 也可以像普通函数一样手动调用
        self.name = name  ## self.name 实例变量
        self.age = age
        print("student_init__!")
        print(self.name,name)
        # return "stu"  ## __init__ 只能返回None！ TypeError: __init__() should return None, not 'str'

    def do_homework(self):
        print("homework!!")
    # def print_file(self):  ##class 的函数中 self是固定的关键字
    #     print(self.name,self.age) ##需要加上self 才能调用 name 和age
        # print(name) ## NameError: name 'name' is not defined 直接调name报错

    ## 定义类方法
    @classmethod
    def plus_summ(qqcls): ##cls约定俗成的命名
        qqcls.summ+= 1
        print("summ:",qqcls.summ)


    # 类只负责定义和刻画，不负责调用和执行
    # print_file()  # TypeError: print_file() missing 1 required positional argument: 'self'


student1  = Student("xin",3)
Student.plus_summ()
student2  = Student("xxx",3)
Student.plus_summ()
# a = Student("g",5).__init__("g",5)
# print(a)
# print(type(a))
print(Student.name)  ##类的name
Student.name = "www"
print(Student.name)
print(student1.name)
print(id(student1),id(student2)) ## id是不同的 3030638171584 3030638171248
print(id(Student))  ## student1，student2 不同，1645930923176

##类方法的调用
Student.plus_summ()
student1.plus_summ() ## 实例对象也可以调用类方法。。


class Printer():

    def print_file(self):  ##class 的函数中 self是固定的关键字
        print(self.name,self.age) ##需要加上self 才能调用 name 和age

# print(dir())