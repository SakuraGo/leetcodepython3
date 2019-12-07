##字符--阿斯克码 互转
print(ord('a')-ord('z'))  ## -25
print(ord('c'))   ## 99
print(chr(97)) # 'a'

## 不相关的矩阵构造
visited = [[0 for i in range(10)] for j in range(15)]

## lambda 排序
lis = [(1,22),(5,2),("q",8),(3,3)]
lis = sorted(lis,key=lambda x:x[1],reverse=True)
print(lis)  ## [(1, 22), ('q', 8), (3, 3), (5, 2)]

print("casdf">'b')

print(list(range(3)))

##判断是否回文
def is_circle(num):
    s = str(num)
    return s == s[::-1]

##求数组区间最大和
def maxqujian(lis):
    maxxx = 0
    sum = 0
    for num in lis:
        sum += num
        maxxx = max(maxxx,sum)
        if sum<0:
            sum = 0
    return maxxx

##由num生成回文 num = 123 ==》 123321,12321
def create_circle(num):  ###  关键是这里，主动生成回文，而非一个个数的盲目遍历。。。。
    s = str(num)
    first = int(s + s[::-1])
    second = int(s[:-1] + s[::-1])
    return first, second

## 求最小公约数
def lcd(x,y):
    if y == 0:
        return x
    else:
        return lcd(y,x%y)

##最小公倍数
a,b= 6,8
ab = a*b / lcd(a,b)
print(ab)

##大质数
dazhishu = 10**9+7
print(dazhishu)

## 从dp[i][j] 表示从i到j的dp
# for k in range(2, lenn):
#     for i in range(0, lenn - k):
#         j = i + k

##二进制表示10个位置的2^10个状态
# for i in range(0, 2 << 10):
#     print(bin(i))


# addr = '%s\\in\\in%s'%(os.getcwd(),date)
