# 1155. 掷骰子的N种方法
# 这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
#
# 我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
#
# 如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。

# 输入：d = 1, f = 6, target = 3
# 输出：1



class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        ccc = 1000000007
        if d * f < target:
            return 0

        if d* f == target:
            return 1

        if d == 1:
            return 1

        dp = [[0 for i in range(target)] for j in range(d)]

        for i in range(min(f,target)):
            dp[0][i] = 1

        for i in range(1,d):
            xianduansum = 0
            for j in range(i,target):
                # start = max(j-d,0)
                if j-f<=0:
                    xianduansum += dp[i-1][j-1]
                else:
                    xianduansum += dp[i-1][j-1]
                    xianduansum -= dp[i-1][j-f-1]
                dp[i][j] = xianduansum % ccc

        print("dpdp:",dp)
        return dp[d-1][target-1]

res = Solution().numRollsToTarget(2,6,7)
print(res)










print(2389571979579172051235%1000000007)