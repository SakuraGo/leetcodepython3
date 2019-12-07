# 5216. 统计元音字母序列的数目  显示英文描述  我的提交返回竞赛
# 题目难度 Hard
# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
#
# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

# 输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
#
# 输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

class Solution:
    def __init__(self):
        self._data = ["a","e","i","o","u"]

    ##递归返回有效的数量..

    def countVowelPermutation(self, n: int) -> int:

        moo = 1000000007
        ##想了想还是DP
        dp = [[0 for j in range(n)] for i in range(5)]
        for i in range(5):
            dp[i][0] = 1 ##初始化

        for j in range(1,n):
            dp[0][j] = (dp[1][j-1] + dp[2][j-1]+dp[4][j-1])%moo  ## a
            dp[1][j] = (dp[0][j-1]+dp[2][j-1])%moo  ## e
            dp[2][j] = (dp[1][j-1]+dp[3][j-1]) %moo ## i
            dp[3][j] = (dp[2][j-1])%moo  ## o
            dp[4][j] = (dp[2][j-1]+dp[3][j-1]) % moo

        res = 0
        for i in range(5):
            res += dp[i][n-1]
        return res%moo

res = Solution().countVowelPermutation(5)
print(res)


