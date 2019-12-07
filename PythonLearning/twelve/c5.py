#reduce

from functools import reduce
list_x = [1,2,3,4,5,6,7,8]
# reduce(func ,sequence,initial=None)

#reduce做连续计算,连续调用lambda
r = reduce(lambda x,y:x+y,list_x)

# 一点点从list_x 中取值计算 ，依据lambda来做维度降低
# 1+2
# 3+3
# 6+4
# 10+5
# 15+6
# 21+7
# 28+9


print(r)

list_xx = ['1','2','3','4','5']
r = reduce(lambda x,y:x+y,list_xx,'abc')  ##‘abc’作为初始值参与计算.
print(r)