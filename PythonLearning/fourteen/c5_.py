##生成器
# print 0 ~ 10000
n = [i for i in range(0,10001)]
# print(n)

# for i in n:
#     print(i)

def gen(max):
    n = 0
    while n<=max:
        # print(n)
        n+=1
        yield n  ## 获得了一个生成器.

g = gen(1000)  ## 生成器可以被迭代，生成器保存的是一个算法，而不是这10000个数字..
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3

print(gen(10000)) # <generator object gen at 0x0000022F60892468>
