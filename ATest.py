# a = [1,2,3,5]
# b = [3,5,1,9,0]
# print(a+b)
# print(a)
# a +=b
# print(a)
# print(a.append(b))
# print("aaa")
# c = [3]
# c.append(5)
# print(c)
#
# d = [5]
# d.append([1,1])
# print(d)

# aaa = [1,2,3,4,5]
# print(aaa[:2])
#
# bbb = [0]*10
# bbbc = bbb*5
# print(bbbc)
#
# cc = [0]*5
# lis = []
# for i in range(3):
#     lis.append(cc.copy())
# print(lis)
# cc[3] = 1
# print(lis)
# lis[2][1] = 2
# print(lis)
#
# print(isinstance(cc,list))

#
# asd = 21
# q =123
# print(asd|q)   ##按01的位置求并集。。。


# print(3<<6)
# asdf = [(1,2),(3,4),(5,6)]
# print(asdf[0:1])

dic = {"a":3,"c":33,"b":2}

#sorted(dic,key=lambda x:x[0])
# dic2 = sorted(dic)  ##默认对dic的键数组,dic.keys()排序
# print(dic2)
#
# dic3 = sorted(dic.items(),key=lambda x:x[1])
# print(dic3)
#
liss = ['a','b','a','c']
se = set(liss)
se.remove('a')

print(se)
#
sett = set()
sett = sett | {'a'}
# sett = {n|{'a'} for n in sett} | {'b'}
print(sett)
#
# temp = set()
# temp.add("a")
# temp.add("a")
# temp.add("b")
# temp.add("q")
#
# for n in temp:
#     print(n)
# temp = set([n | {'a'} for n in temp])
#
# print(temp)

##多维数组创建
# m = [[0] * 3] * 10  ##反例
# m[1][2] = 23
# print(m)
#
#
# image =[[(col+1)*(row+1) for col in range(5)] for row in range(3)]
# image[1][2] = 333
# print(image)
#
# vivi = [[[0 for i in range(3)]for j in range(2)]for k in range(3)]
# vivi[0][1][2] = 333
# print(vivi)
#
# asdf= 'qwertt'
# print(asdf[2])

#dic = {1:"asd"}
# dic[2] = {'q'}
# print(dic)
#
# lis = []
# lis.append(dic)
# print(lis)

# dic = {31:3,22:23}
#
# for key,val in dic.items():
#     print(key,val)
#
# for index,item in enumerate(dic.items()):
#     print(index,item)

# 在有些时候，我们可能会遇到字符之间的距离计算。在C语言中允许两个字符使用‘-’运算符，但是python不支持这个操作。
# python的ord()函数参数是一个字符，返回值是该字符对应的ascii码。
# print(ord('a')-ord('z'))
# print(ord('c'))
# print(chr(97)) # 'a'

# asdf = "qwer"
# print(asdf[:-1])  ## "qwe"
#
# asdfte= [2,3,5,6]
# print(asdfte[8:12])
# memo = asdfte[1:3]
# print(memo)
# memo[0] = 3333
# print(memo)
# print(asdfte)
# asdfte[1:3] = memo
# print(asdfte)
# from heapq import *
# asdf = set([1,3,3,5])
# print(asdf)
# print(len(asdf))
# h = heapify(list(asdf))
# print(h)
#
#
# import math
# from io import StringIO
#
# import heapq
# from heapq_showtree import show_tree
# # from heapq_heapdata import data
# data = [19, 39, 4, 110, 511]
# heap = []
# print('random :', data)
# print()
#
#
# # for n in data:
# #     print('add {:>3}:'.format(n))
# #     heapq.heappush(heap, n)
# #     # show_tree(heap)
#
# res  = heapq.heapify(data)
# print(res)
# print(data)
# res = heapq.heappop(data)
# print(res)
# print(data)
# heapq.heappushpop(data,335)
# print(data)
#
# import itertools
# list1 = [1,2,3,4,5]
# for item in itertools.product(list1,list1):
#     print(item)


# import torch.nn.functional as F
# import torch
#
# out = torch.Tensor([[0, 0, 0], [3, 0, 1]])  ##shape 为 (N,C), C代表分类类别数
# target = torch.LongTensor([0, 2])   ## target 的分类数不能超过C
#
# loss = F.cross_entropy(out, target)
# print(loss)
#
#
#
# loss = F.cross_entropy(out,target,reduction='sum')
# print(loss)
#
#
#
# loss = F.cross_entropy(out,target,reduction='none')
# print(loss)
#
# a = torch.randn(4, 4)
# print(a)
# print()
# b = torch.max(a,1,keepdim=True)
# print(b)

# diccc = {"a":(1,2),"b":(3,50),"dd":(5,13)}
# print(diccc.items())
# asdf =  sorted(diccc.items(),key=lambda x:x[1][0],reverse=True)
# print(asdf)

# aa = [1,2,3,"q"]
# bb = [1,2,3,"q"]
# print(aa == bb)

# for i in  range(10,-1,-1):
#     print(i)

# asdf = [[1,2,3],[4,5,6]]
#
# print(asdf)
# print(type(asdf))
#
# import numpy as np
# asdf = np.array(asdf)
# print(asdf)
#
# bbb = np.array([0.1,0.2,0.3])
# print(asdf+bbb)



print(200*300*400*500*600*700*800*900*1000)
print(2**19)
print(2**14)
print(2**16)
print(2**17)

tt = (1,2,3)

print(tt,tt[2])

# tt[1] = 2 ## 不可改变

a =  [7,8,3]
import bisect
b = bisect.bisect(a,6)
print(b)

class Sol():
    def __init__(self):
        print("qq")

    def add(self,a,b):
        print("ab",a+b)

class ASD():
    def teesttt(self):
        Sol().add(1,3)

asd = ASD().teesttt()

lis = [[1,2],[3,4]]
print([3,4] in lis)