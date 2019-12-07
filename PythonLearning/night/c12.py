class Student():
    summ = 0
    name = "wang" ##类变量
    age  = 0

    ## 左右都有双下划线的，是public的，不过是python内置的方法的标志.
    def __init__(self,name,age): ##初始化函数/构造函数
        Student.summ+= 1
        self.name = name  ## self.name 实例变量
        self.age = age
        self.__score = 0

    ##认为 __ 开头的方法是私有的

    def marking(self,score):
        if score<0:
            return "不能够打负分"
        self.__score = score
        print(self.name+"同学本次考试分数:",score)



    def do_homework(self):
        print("homework!!")
        self.do_english()

    def do_english(self):
        print("english")

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

stu1.do_homework() ##外部方法
# stu1.score = -1 ##不安全的操作

stu1.marking(69)
# res = stu1.marking(-1)
# 公开的public 私有的private

# print(res)
stu1.__score = 35  ## 还是可以访问..??  python添加了新的实例变量..
print(stu1.__score)
print(stu1.__dict__)  ## {'name': 'wzy', 'age': 18, '_Student__score': 69, '__score': 35}
## _Student__score就是python存的私有变量__score. 而'__score': 35 是上一步新建的变量

stu2 = Student("zzz",20)
print(stu2.__dict__) ## {'name': 'zzz', 'age': 20, '_Student__score': 0}
print("曲线读取私有变量__score: ",stu2._Student__score)
print(stu2.__score)
##  'Student' object has no attribute '__score'