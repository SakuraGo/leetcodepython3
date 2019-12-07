from PythonLearning.night.c14_ import Human
class Student(Human): ##People是父类
    # summ = 0


    ## 左右都有双下划线的，是public的，不过是python内置的方法的标志.
    def __init__(self,school,name,age): ##构造函数就需要有3个参数
        self.school = school
        # Human.__init__(self,name,age)  ##需要传入self ,这里是通过类来调用__init__构造函数，必须明确self
        super(Student,self).__init__(name,age) ## 使用super调用父类


    def marking(self,score):
        if score<0:
            return "不能够打负分"
        self.__score = score
        print(self.name+"同学本次考试分数:",score)



    def do_homework(self):  ## 一般的实例对象调用self，不需要传入self，默认该实例对象就是self
        print("homework!!" ,end="")
        self.do_english()
        super(Student, self).do_homework() ##调用了父类的do_homework方法


    def do_english(self):
        print("english")

stu1 = Student("人民路小学","石敢当",18)
# Student.do_homework()  ## TypeError: do_homework() missing 1 required positional argument: 'self'
## 用类调用 python不知道 self是谁
# Student.do_homework(stu1)
stu1.do_homework() ## 子类与父类方法同名，优先调用子类的..
# print(stu1.sum)
# print(Student.sum)
print(stu1.name)
print(stu1.age)

