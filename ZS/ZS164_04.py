# 5274. 停在原地的方案数  显示英文描述  我的提交返回竞赛
# 用户通过次数 140
# 用户尝试次数 198
# 通过次数 143
# 提交次数 404
# 题目难度 Hard
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
#
# 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
#
# 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
#
# 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

# 输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
from  typing import  List
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        # print(mod)
        if arrLen == 1:
            return 1
        dp = [[0 for jj in range(min(arrLen,steps))] for ii in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(2, len(dp)):
            for j in range(0, len(dp[0])):
                dp[i][j] += dp[i-1][j]
                if j>0:
                    dp[i][j] += dp[i-1][j-1]
                if j<len(dp[0])-1:
                    dp[i][j] += dp[i-1][j+1]

                dp[i][j] = dp[i][j] % mod

        return dp[-1][0]

res = Solution().numWays(4,2)

print(res)