# 5090. 抛硬币  显示英文描述  我的提交返回竞赛
#
# 你有一些不规则的硬币。第 i 枚硬币正面朝上的概率是 prob[i]。
#
# 请你抛掷每个硬币恰好一次，返回正面朝上的硬币数等于 target 的概率。

# 输入：prob = [0.4], target = 1
# 输出：0.40000

# 输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# 输出：0.03125

from  typing import List
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        dp = [[0 for j in range(len(prob))] for  i in range(target+1)]


        for idx,probbb in enumerate(prob):
            if idx == 0:
                dp[0][0] = 1 - probbb
            else:
                dp[0][idx] = dp[0][idx-1]*(1-probbb)

        if target == 0:
            return dp[0][-1]

        dp[1][0] = prob[0]
        for i in range(2,len(dp)):
            dp[i][i-1] = dp[i-1][i-2]*prob[i-1]

        ##dp递推。。
        for i in range(1,len(dp)):
            for j in range(i,len(prob)):
                dp[i][j] = dp[i][j-1]*(1-prob[j]) + dp[i-1][j-1]*prob[j]
        # print(dp)

        return dp[target][-1]

res = Solution().probabilityOfHeads([0.2,0.8,0,0.3,0.5],3)
print(res)
