a = [1,2,3,4,5,6]
b = [1,2,3]
c = a*3 + b + a
print(c)
c [2] = 100
print(c)

a = 1   ## a = 1 把a指向1
b = a   ## a与b指向同一个不可变类型 int 1 ，a变了(指向3)  b不变
a = 3   ## 这一步 并不是把a的值改变了，而是新生成一个3，让a再指向3..
print("b:",b)

a = [1,2,3,4,5]
b = a
a[0] = "235"
print(b)   ## a与b指向同一个可变类型list ，list变了a与b一起变

'''
不可变类型: int,str,tuple
可变类型: list,set,dict

'''
a = 123
print("id a:",id(a)) ## id a: 1749908320
a = 125
print("id a:",id(a)) ## id a: 1749908384

## id(a) a在内存中的存储位置.
a = 1
b = 1
print(id(a))  ## 1749904416
print(id(b))  ## 1749904416  ##相同！

a = [1,23,5]
print(id(a))  ## 1518605934856
a[2] = 666   ## 字典可变，因此当字典a改变后，内存位置没变
print(id(a))  ## 1518605934856
print(a)

# c = (1,2,3)
# c.append(4)
aa = [1,2,3]
aa.append(4)
print(aa)

abc = (1,2,3,[4,5,6])  ## 元组中的list依然是可变的
abc[3].append(56)
print(abc)
##以下输出4个不同的id
print(id(abc[0]))
print(id(abc[1]))
print(id(abc[2]))
print(id(abc[3]))
print()
##算术运算符
print(3-1)
print(3/2)
print(3//2) ## 保留整数部分
print(5%2) ##余数
print(3**2) ##平方
print(2**5) ## **n n次方

# 赋值运算符
# +=
# *=
# -=
# /=
# %=
# **=
# //=

# 比较(关系)运算符
# ==
# !=
# >
# <
# >=
# <=
print()
print(1<=2)
print(1!=3)

w = 1
w+=w>=1  ##  int 可以和 bool类型相加，int(True)等于1
print(w)

print("abc"<"abd") # True
print(ord("c"),ord("d")) ## 99 100
## str,list 和元组都可以比较
print([1,2,3]<[2,3,4]) # True
print((1,2,3)<(1,3,2))  ## True
d1 = {1:1}
d2 = {2:2}

print()
# print(d1<d2) ## TypeError: '<' not supported between instances of 'dict' and 'dict'

## 逻辑运算符
# and ,
# or,
# not

print(True and True)
print(False and True)
print(False or True)
print(False or True and True) ## True
print(not True)
print(not True or False)
print()
print(not not True)
print(1 and 1)   ## True and True
print("a" and "b")  #"b"
print("a" or "b")  # "a"

## int float  0 被认为False, 非0 表示 True
print(not 0.1) ## False
## str 空字符串 False， 否则 True
print(not "")  ## not False  # True

## list 空的列表为False
print(not [])
print(not [1,2])
## 空的tuple，dict 为False

print()
print([1] or []) ##[1]
print([] or [1]) ##[1]

print()
print("a" and "b")  ## "b"
print("" and "b")  ## ""

## and or 返回规律
print(1 and 0)
print(0 and 1)
print(1 and 2)
print(1 or 2) ## 1 第一个1 已经可以判定最后结果是True ，所以返回1
print(1 and 2) ## 2 ## and 需要2个都知道才能确定是否是True，所以返回第二个
print(0 and 2) # 0

print()
## 成员运算符
print( 1 in [1,2,3,5]) #True

b = "a"
print(b in {"c":1})
b  =1
print(b in {"c":1})
b = "c"
print(b in {"c":1})  ##对于 b in dict 来说，是在查看字典的key中是否有该元素

print(1 in {"c":1}.values()) ##True

print("身份运算符")
a = 1
b = 2
print(a is b)
a = 1
b = 1
print(a is b)
a = "hello"
b = "world"
print(a is b)
c  ="hello"
print(a is c)

a = 1
b = 1.0
print( a == b) ## True
print(a is b)  ## False
## is 不是比较值相等，is 比较的是两个变量的神风是否相等 (比较内存地址)
print(id(a),id(b)) ## 1749904416 2609605645128
print(a is not b)

a = {1,2,3}
b = {2,1,3}
print(a == b)  ## True  ## 集合是无序的
print(a is b)  ## False
print(id(a),id(b))  ## 2724724419720 2724724716936 ##内存地址不同
c = (1,2,3)
d = (2,1,3)
print(c == d)  ## False  ##元组是讲究顺序性的，是有序的
print(c is d)  ## False
print(id(c),id(d))  ## 2724724619808 2724724532640 ## 内存地址不同

# a = 1
# b = 2
# print(a== b)
# print(a is b)
##  值(value) ，身份(id)，类型(type) 是对象的三个特征
##  ==       ,  is      isinstance  来判断
##  python万物皆对象
a = 1
print(type(a) is int) # True
print(type(a) == int) # True
print(type(a) == str) # False
a = "hello"
##判断变量类型的函数
isinstance(a,int)
print(isinstance(a,str)) ##True
print(isinstance(a,(int,str,float))) ## True ##是否是元组中的任意一种类型
print(isinstance(a,(int,float))) ## False

ad = [1,2,3]
addd = [1,2,3]
print(id(ad),id(addd)) ##2522531997192 2522531995912 不同.

ss1 = "ss"
ss2 = "ss"
print(id(ss1),id(ss2)) ## 2330875479408 2330875479408 相同

print()
print("位运算，把数字当做二进制数进行运算")
#& 按位与
#| 按位或
#^ 按位异或
#~ 按位取反
#<< 左移动
#>> 右移动

a = 2 #10
b = 3 #11
print(a&b)  # 2
print(2|3)  # 3
print(335>>4)
print(1<<3)