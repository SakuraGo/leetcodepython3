class Student():
    summ = 0
    name = "wang" ##类变量
    age  = 0

    def __init__(self,name,age): ##初始化函数/构造函数
        Student.summ+= 1
        self.name = name  ## self.name 实例变量
        self.age = age


    def do_homework(self):
        print("homework!!")

    ## 定义类方法
    @classmethod
    def plus_summ(qqcls): ##cls约定俗成的命名
        qqcls.summ+= 1
        print("summ:",qqcls.summ)


    ## 定义静态方法
    ## 没有强制传入self，就是一个普普通通的方法.
    ## 类可以调用，对象也可以调用
    @staticmethod
    def add(x,y):
        # print(name)
        print(Student.summ)
        print("This is a Static method....")


stu1 = Student("wzy",18)
stu1.add(1,2)
Student.add(3,5)
# stu1.plus_summ()
Student.plus_summ()
Student.plus_summ()
Student.plus_summ()