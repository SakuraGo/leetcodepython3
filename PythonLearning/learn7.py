varrr = 1
while varrr <= 10:
    print(varrr)
    varrr+=1
else:
    print("final:var=",varrr)


## for 循环主要用来遍历/循环 序列或者集合、字典
a = ['apple',"orange","banana"]
for x in a:
    print(x)

aa  = [['apple',"orange","banana"],(1,2,3)]
for x in aa:
    for y in x:
        print(y,end="") ##不换行打印 appleorangebanana123
        if y == "orange":
            break
    else:
        print("二层EOF")
else: ##全部被遍历完了之后就会触发. break中断不会触发..
    print("fruit is gone!")

print()

print("for循环 ")
for i in range(0,10):
    print(i)
print()
for i in range(0,10,2):
    print(i,end=" | ")
print()
for x in  range(10,0,-2):
    print(x ,end=" | ")
print()
a = [1,2,3,4,5,6,7,8]
for idx,x in enumerate(a):
    if idx%2 == 0:
        print(x,end=" | ")

print()
b = a[0:len(a):2]
print(b)

# from PythonLearning.t import c7
# print(c.a)  ## 2

# from PythonLearning.t import c7 as ccc
# print(ccc.a )  ## 2

from t.c7 import a ##这样也行。。
print(a)

from t.c7 import  *

print("a:",a)
print("b:",b)
print("c:",c)

# print("d:",d)

print()

