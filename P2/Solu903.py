# 903. DI 序列的有效排列  显示英文描述
# 题目难度 Hard
# 我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）
# 有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：
#
# 如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；
# 如果 S[i] == 'I'，那么 P[i] < P[i+1]。
# 有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7.

# 输入："DID"
# 输出：5
# 解释：
# (0, 1, 2, 3) 的五个有效排列是：
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)

from typing import List
class Solution:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(S)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                if S[i - 1] == 'D':
                    for k in range(j, i + 1):
                        # here start from j, regard as swap value j with i, then shift all values no larger than j
                        dp[i][j] += dp[i - 1][k]     ##强大的递推公式，然而这个题的主要难点更在于设计出dp[i][j]的含义：考虑到第i个字符，且结尾的数==j的个数 。。。。
                                                        # 方便了之后的递推，只要分2种情况讨论即可
                        dp[i][j] %= mod
                else:
                    for k in range(0, j):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
        print(dp)
        return sum(dp[n]) % mod

res = Solution().numPermsDISequence('DID')
print(res)