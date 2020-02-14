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

##取二进制某一位..
# for i in xrange(len(bin_num)):
#         if (1<<i) & int_num:
#              print " the number '1' position is "+str(i)

#计算二进制数中1的个数
def countOnes1(x):
    count = 0
    while x > 0:
        if x & 1 == 1:
            count += 1
        x >>= 1

    return count

def get_bit_val(byte, index):
    """
    得到某个字节中某一位（Bit）的值

    :param byte: 待取值的字节值
    :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :returns: 返回读取该位的值，0或1
    """
    if byte & (1 << index):
        return 1
    else:
        return 0


def set_bit_val(byte, index, val):
    """
    更改某个字节中某一位（Bit）的值

    :param byte: 准备更改的字节原值
    :param index: 待更改位的序号，从右向左0开始，0-7为一个完整字节的8个位
    :param val: 目标位预更改的值，0或1
    :returns: 返回更改后字节的值
    """
    if val:
        return byte | (1 << index)
    else:
        return byte & ~(1 << index)