# 474. 一和零
# 在计算机界中，我们总是追求用有限的资源获取最大的收益。
#
# 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
#
# 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
#
# 注意:
#
# 给定 0 和 1 的数量都不会超过 100。
# 给定字符串数组的长度不会超过 600。
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
#
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        memo = [None] * len(strs)
        for i in range(len(strs)):
            memo0 = [None] * (n + 1)
            for j in range(n + 1):
                memo0[j] = [0] * (m + 1)
            memo[i] = memo0

        dataLis = []

        for str in strs:
            mCnt0 = str.count('0')
            nCnt1 = str.count('1')
            dataLis.append([mCnt0, nCnt1])

        firstData = dataLis[0]
        # print("data:%s" % dataLis)
        for i in range(len(memo[0])):
            for j in range(len(memo[0][0])):
                if i >= firstData[1] and j >= firstData[0]:
                    memo[0][i][j] = 1

        layerC = 1

        while (layerC < len(dataLis)):
            # print(layerC)
            newM0, newN1 = dataLis[layerC]

            firLayer = memo[layerC - 1]
            newLayer = memo[layerC]
            for ii in range(len(memo[1])):
                for jj in range(len(memo[1][0])):

                    ##不选
                    buxuanCnt = firLayer[ii][jj]
                    ##选择
                    xuanCnt = 0
                    if ii - newN1 >= 0 and jj - newM0 >= 0:
                        xuanCnt = 1 + firLayer[ii - newN1][jj - newM0]
                    memo[layerC][ii][jj] = max(buxuanCnt, xuanCnt)
            layerC += 1
        return memo[len(strs) - 1][n][m]

'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        memo = [None]*2
        for i in range(2):
            memo0 = [None]*(n+1)
            for j in range(n+1):
                memo0[j] = [0] * (m+1)
            memo[i] = memo0

        dataLis = []

        for str in strs:
            mCnt0 = str.count('0')
            nCnt1 = str.count('1')
            dataLis.append([mCnt0,nCnt1])

        firstData = dataLis[0]
        print("data:%s"%dataLis)
        for i in range(len(memo[1])):
            for j in range(len(memo[1][0])):
                if i>= firstData[1] and j >= firstData[0]:
                    memo[0][i][j] = 1

        layerC = 1

        while(layerC < len(dataLis)):
            print(layerC)
            newM0,newN1 = dataLis[layerC]

            firLayer = memo[0]
            newLayer = memo[1]
            for ii in range(len(memo[1])):
                for jj in range(len(memo[1][0])):

                    ##不选
                    buxuanCnt = firLayer[ii][jj]
                    ##选择
                    xuanCnt = 0
                    if ii-newN1>=0 and jj-newM0>= 0:
                        xuanCnt = 1 + memo[0][ii-newN1][jj-newM0]
                    memo[1][ii][jj] = max(buxuanCnt,xuanCnt)
            layerC += 1
            print(memo[0])
            print("layerC:%d"%layerC)
            memo[0] = newLayer.copy()
            print(memo[0])


        print("-=----")
        print(firLayer)
        print(newLayer)
        return memo[0][n][m]



'''
res = Solution().findMaxForm(["10","0001","111001","1","0"],5,3)
print(res)
# memo0 = []
# for i in range(5):
#     row = [0] * 7
#     memo0.append(row)
# memo0[3][5] = 23
# memo1 = memo0.copy()
# memo1[1][2] =123
# print(memo0)
# print(memo1)

# memo = [None]*2
# for i in range(2):
#     memo0 = [None]*3
#     for j in range(3):
#         memo0[j] = [0] * 5
#     memo[i] = memo0
# memo[1][1][3] = 11
#
# # memo[0] = memo[1]
# qwer = memo[1]
# memo[1][1][1] = 23
#
# print(memo)