class Student():
    name = "wang" ##类变量
    age  = 0
    summ = 0



    ##实例方法 有一个参数self
    def __init__(ssgsr,name,age): ##初始化函数/构造函数 ## self可以换成this或者其他的命名
        ssgsr.name = name  ## 这样是不能改变类变量的！
        ssgsr.age = age
        print("名字+年龄：",name,age)
        Student.summ += 1



    def do_homework(self):
        print("homework!!")
        print(self.name)

    def ddddd(asdf):
        print(asdf.age)
        print("类变量summ：",asdf.__class__.summ)

stu1 = Student("石敢当",18)
print(stu1.name)  ## 首先查找stu1中有没有name，再查找Student类中有没有name，再没有找父类
print("Stu_sum",Student.summ)
print(Student.name)
stu2 = Student("王菲",28)
print("Stu_sum",Student.summ)
stu2.do_homework()
stu2.ddddd()
print(stu1.__dict__) ## dict 保存着 stu1的所有变量
## 加了self.name 之后：{'name': '石敢当', 'age': 18}
## 不加self {}

print(Student.__dict__) ## dict 保存着 stu1的所有变量
## {'__module__': '__main__', 'name': 'wang', 'age': 0,
# '__init__': <function Student.__init__ at 0x000002563DE47400>,
# 'do_homework': <function Student.do_homework at 0x000002563E0FE268>,
# '__dict__': <attribute '__dict__' of 'Student' objects>,
# '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}