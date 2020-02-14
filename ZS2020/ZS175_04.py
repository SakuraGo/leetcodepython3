# 5335. 参加考试的最大学生数  显示英文描述
# 用户通过次数 0
# 用户尝试次数 1
# 通过次数 0
# 提交次数 1
# 题目难度 Hard
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
#
# 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
#
# 学生必须坐在状况良好的座位上。

# 输入：seats = [["#",".","#","#",".","#"],
#               [".","#","#","#","#","."],
#               ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。

from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        m = len(seats)
        n = len(seats[0])

        def countOnes1(x):
            count = 0
            while x > 0:
                if x & 1 == 1:
                    count += 1
                x >>= 1

            return count

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
        def keyideZuowei(num0, lennn: int):

            comLisNum = (1 << lennn) - 1
            idx = 0
            while num0 > 0:
                if (num0 & 1) == 1:
                    if idx - 1 >= 0:
                        comLisNum = set_bit_val(comLisNum, idx - 1, 0)
                    if idx + 1 < lennn:
                        comLisNum = set_bit_val(comLisNum, idx + 1, 0)
                num0 >>= 1
                idx += 1

            print("comLisNum:",comLisNum)
            return comLisNum


        validNum = []

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

        def dfs(lis: List[str], idx: int, tempNum: int):
            # print(idx,tempNum)
            if idx >= len(lis):
                ##到底的判断
                if tempNum > 0:
                    validNum.append(tempNum)
                    return

            if idx < len(lis):
                if lis[idx] == '#':
                    dfs(lis, idx + 1, tempNum)
                elif lis[idx] == '.':
                    ##取1
                    if idx == 0:
                        dfs(lis, idx + 1, tempNum + (1 << idx))

                    if idx > 0 and get_bit_val(tempNum, idx - 1) == 0:  ##判断上一位是否是1
                        ##可以取1
                        dfs(lis, idx + 1, tempNum + (1 << idx))

                    ##取0
                    dfs(lis, idx + 1, tempNum)

        validNum.append(0) ##加上空行这个选项

        # print(seats[0])
        dfs(seats[0],0,0)
        print('Valid:',validNum)

        resMemo = [[] for i in range(m)]
        resMemo[0] = validNum
        print('rrrr',resMemo)



        for i in range(1,m): ##遍历第二到最后一行
            print("第 %i 层",i)
            rowSeats = seats[i]
            preValidNum = resMemo[i-1]
            validNum = []

            dfs(seats[i],0,0)
            validNum.append(0)
            print(validNum)

            ##遍历valid,给每个valid数配一个在preValid中合理的最大数

            for num in validNum:
                # print(num)
                maxx = -1
                biggestN = -1
                compNum1 = keyideZuowei(num, n)
                print("num:::::,", bin(num), '\n可以的座位:', bin(compNum1))
                for preN in preValidNum:
                    compNum0 = preN>>((i-1)*n)
                    # print("之前的数：",compNum0)

                    if compNum1 | compNum0 == compNum1:
                        ##符合的数
                        if countOnes1(preN)>maxx:
                            maxx = countOnes1(preN)
                            biggestN = preN
                newValidNum = biggestN+(num<<(i*n))

                print(num,' 对应最大的数:',maxx,' ',biggestN)
                print("新增的数:", newValidNum)
                resMemo[i].append(newValidNum)

        print("ResMemo:",resMemo)

        res = max([countOnes1(aaa) for aaa in resMemo[-1]])
        for resss in resMemo[-1]:
            print("二进制:",bin(resss))

        return res

# a = 12
# print(a)
# print(a<<1)
# print(a>>1)

res = Solution().maxStudents([[".","#","#","."],[".",".",".","#"],[".",".",".","."],["#",".","#","#"]])
print(res)

# for i in range(0, 2 << 10):
#     print(bin(i))

# for i in range(10):
#         if (1<<i) & 8:
#              print (" the number '1' position is "+str(i))

# print(0 is not True)

# def set_bit_val(byte, index, val):
#     """
#     更改某个字节中某一位（Bit）的值
#
#     :param byte: 准备更改的字节原值
#     :param index: 待更改位的序号，从右向左0开始，0-7为一个完整字节的8个位
#     :param val: 目标位预更改的值，0或1
#     :returns: 返回更改后字节的值
#     """
#     if val:
#         return byte | (1 << index)
#     else:
#         return byte & ~(1 << index)
# def keyideZuowei(num0, lennn: int):
#     print("~~~~~")
#     comLisNum = (1 << lennn) - 1
#     idx = 0
#     while num0>0:
#         if (num0&1) == 1:
#             # set_bit_val(num0,)
#             if idx-1>=0 :
#                 comLisNum = set_bit_val(comLisNum,idx-1,0)
#             if idx+1< lennn:
#                 comLisNum = set_bit_val(comLisNum,idx+1,0)
#         num0>>= 1
#         idx+=1
#
#     print(comLisNum)
#     return comLisNum
#
# print(keyideZuowei(0b10001,5))
#
#
#
# print(set_bit_val(7,9,1))
# print(~(1 << 3))
# print(~1)  ## -2 补码形式。。


# validNum = []
# def get_bit_val(byte, index):
#     """
#     得到某个字节中某一位（Bit）的值
#
#     :param byte: 待取值的字节值
#     :param index: 待读取位的序号，从右向左0开始，0-7为一个完整字节的8个位
#     :returns: 返回读取该位的值，0或1
#     """
#     if byte & (1 << index):
#         return 1
#     else:
#         return 0
# def dfs(lis: List[str], idx: int, tempNum: int):
#     # print(idx,tempNum)
#     if idx >= len(lis):
#         ##到底的判断
#         if tempNum > 0:
#             validNum.append(tempNum)
#             return
#
#     if idx < len(lis):
#         if lis[idx] == '#':
#             dfs(lis, idx + 1, tempNum)
#         elif lis[idx] == '.':
#             ##取1
#             if idx == 0:
#                 dfs(lis, idx + 1, tempNum + (1 << idx))
#
#             if idx > 0 and get_bit_val(tempNum,idx-1) == 0:  ##判断上一位是否是1
#                 ##可以取1
#                 dfs(lis, idx + 1, tempNum + (1 << idx))
#
#             ##取0
#             dfs(lis, idx + 1, tempNum)
#
#
#
# # dfs([".",".",".","#"],0,0)
# # print(validNum)
#
# print(8 is not True)