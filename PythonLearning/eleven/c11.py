def f1():
    a = 10
    def f2():
        a  = 20  ## 被python认为是局部变量
        print(a)
    print(a)
    f2()
    print(a)

f1()

# 10
# 20
# 10