# 5233. 规划兼职工作  显示英文描述  我的提交返回竞赛
# 用户通过次数 43
# 用户尝试次数 73
# 通过次数 45
# 提交次数 111
# 题目难度 Hard
# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
#
# 注意，时间上出现重叠的 2 份工作不能同时进行。
#
# 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

# 输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# 输出：120
# 解释：
# 我们选出第 1 份和第 4 份工作，
# 时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
from typing import  List
class Solution:
    ##超时..
    def __init__(self):
        self._res = 0
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        all_data = []
        for idx in range(len(endTime)):
            all_data.append((startTime[idx],endTime[idx],profit[idx]))

        all_data = sorted(all_data,key=lambda x:x[1])
        # print(all_data)
        startTime = [all_data[i][0] for i in range(len(all_data))]
        endTime = [all_data[i][1] for i in range(len(all_data))]
        profit = [all_data[i][2] for i in range(len(all_data))]


        dp = [[0 for j in range(all_data[-1][1]+1)] for i in range(len(profit))]
        ##初始化
        for j in range(len(dp[0])):
            if j < endTime[0]:
                continue
            else:
                dp[0][j] = profit[0]

        self._res = max(self._res,profit[0])

        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if j < endTime[i]: ##只能不加入这个profit
                    dp[i][j] = dp[i-1][j]
                elif j == all_data[i][1]:
                    dp[i][j] = max(dp[i-1][j],dp[i][all_data[i][0]]+all_data[i][2])
                    self._res = max(self._res, dp[i][j])
                else:
                    dp[i][j] = dp[i][j-1]


        # print(dp)
        return self._res

res = Solution().jobScheduling([6,15,7,11,1,3,16,2],[19,18,19,16,10,8,19,8],[2,9,1,19,5,7,3,19])
print(res)

testA = [9,8,7,5,3,2,1]
testC = ["q","q","a","b","c","d","e"]
# testC = sorted(testC, )
# print(testC)

zzz = zip(testA,testC)
print(zzz)
