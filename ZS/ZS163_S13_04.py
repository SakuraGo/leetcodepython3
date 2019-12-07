# 5125. 不相交的握手  显示英文描述  我的提交返回竞赛
# 用户通过次数 14
# 用户尝试次数 22
# 通过次数 14
# 提交次数 31
# 题目难度 Hard
# 偶数 个人站成一个圆，总人数为 num_people 。每个人与除自己外的一个人握手，所以总共会有 num_people / 2 次握手。
#
# 将握手的人之间连线，请你返回连线不会相交的握手方案数。
#
# 由于结果可能会很大，请你返回答案 模 10^9+7 后的结果。

class Solution:
    def numberOfWays(self, num_people: int) -> int:
        ##dp把。。
        mod = 10**9+7
        # print(mod)
        dp = [0 for i in range(1050)]
        dp[2] = 1
        dp[4] = 2
        for num in range(6,num_people+1):
            if num%2 != 0:
                continue
            else:
                cur = 0
                cur += dp[num-2]*2 ## 临近点分割。。
                shenyupoints = num-2
                for i in range(2,num-1,2): ##步长为2
                    cur += dp[i]*dp[shenyupoints-i]
                dp[num] = cur % mod
        return dp[num_people]
mod = 10**9+7

print(mod)

res  = Solution().numberOfWays(8)
print(res)