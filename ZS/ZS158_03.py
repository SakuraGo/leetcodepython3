# 5224. 掷骰子模拟  显示英文描述  我的提交返回竞赛
# 题目难度 Medium
# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
#
# 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
#
# 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
#
# 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。

from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        bigzhishu = 10**9 + 7
        maxx = max(rollMax)
        dp = [[[0 for j in range(maxx)] for i in range(6)] for k in range(n)]
        ##初始化 。。
        for i in range(6):
            dp[0][i][0] = 1

        for layer in range(1,n):
            allSum = 0
            for i in range(6):
                allSum += sum(dp[layer-1][i])
            allSum %= bigzhishu
            for i in range(6):
                dp[layer][i][0] = allSum - sum(dp[layer-1][i])
                curMax = rollMax[i]
                for j in range(1,curMax):
                    dp[layer][i][j] = dp[layer-1][i][j-1]

        lastSum = 0
        for i in range(6):
            lastSum += sum(dp[-1][i])
        return lastSum%bigzhishu






        return 1


asdf = [1,2,3,5]
print(max(asdf))