lis = ["新月打击","苍白之瀑","月之降临","月神冲刺"]
print(lis[-1])   #月神冲刺
print(lis[-1:])  #['月神冲刺']  有冒号的会返回一个list

lis2 = ["点燃","虚弱"]
print(lis+lis2)
print(lis2*3)  #['点燃', '虚弱', '点燃', '虚弱', '点燃', '虚弱']
# print(lis2- ["点燃"])  ##TypeError: unsupported operand type(s) for -: 'list' and 'list'

## -- 元组 -- ##
print((1,2,3,4,5))
print((1,"qwe",True))
print((1,2,3,4,5)[2])
print((1,"qwe",True)[2])
print((1,2,3)+(4,5,6))
print((1,"qe",3)*3)

aaa = (1,2,3,4)
for a in aaa : ##元组也可以遍历
    print(a)

print(type((1,2,3)))  ##<class 'tuple'>

print(type((1)))
print(type("qwer"))
print(type(("qwer")))  ##<class 'str'> 预期是 显示元组，因为元组的小括号和进行数学计算的时候的小括号是相互冲突的了。。(1+1)*2
## 括号里只有一个元素的话会被认为是要做数学运算..
print()
# print(type(2,1))  ##没收输出。。。
print(type((2,))) #假装是一个元组 输出判断为元组
print(type(()))  ##空元组

## str list tuple 序列
## 序列的一些共有操作
print("hello world"[2])
print([1,23,3,4,55][0:3])
print([1,23,3,4,55][-1:])
print("hello world"[0:8:2 ])

print()
print(3 in [1,2,3])
print(10 in [3,4,5])
print(3 not in [1,2,3])
print()
print(len("qwer"))
print(max([2,3,5,11,23,5]))
print(max("qwerg"))
print(min((23,3,1)))

print()
##阿斯克码 ascii
print(ord("w"))
print(ord("d"))
print(ord("3"))

print()

## set 集合 set是无序的
print(type({1,2,3,4,5}))
# print({1,2,3,4,5}[2]) #'set' object does not support indexing
print(({1,2,3,4,55,5,5,3,2,1,5}))
print(len({2, 3, 5, 6})) ## 集合可以有len

print("go" in "good") ## true
print({1,2,3,4,5,6} - {3,4,9})  ##差集
print({1,2,3,4,5,6} & {3,4,9})  ##交集
# print({1,2,3,4,5,6} + {3,4,9}) ## TypeError: unsupported operand type(s) for +: 'set' and 'set'
print({1,2,3,4,5,6} | {3,4,9}) ##并集
print(type({}))  ## <class 'dict'>   {} 空字典
print(type(set()))  #空集合
print(len(set()))  ## 长度为0

## dict
print(type({1:1,2:2}))
print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺"})
print({"Q":"新月打击","W":"苍白之瀑","E":"月之降临","R":"月神冲刺"}["Q"])
print({"Q":"新月打击","Q":"苍白之瀑","E":"月之降临","R":"月神冲刺"}["Q"])  ##第二个Q顶掉了第一个Q
print({1:"新月打击","1":"苍白之瀑","E":"月之降临","R":"月神冲刺"}[1])
print({1:"新月打击","1":"苍白之瀑","E":"月之降临","R":"月神冲刺"}["1"])

## value : str int float list set dict  字典的value可以是python的任意的数据类型
## key : 必须是不可变的类型.. eg : int , str
## key 不能是 dict ,list ,但是元组可以是key
# print({{1:1}:"新月打击","1":"苍白之瀑","E":"月之降临","R":"月神冲刺"}) ##unhashable type: 'dict'
print({(1,1):"新月打击","1":"苍白之瀑","E":"月之降临","R":"月神冲刺"})