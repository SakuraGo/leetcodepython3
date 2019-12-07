# 5139. 第 N 个泰波那契数  显示英文描述
# # 用户通过次数 0
# # 用户尝试次数 0
# # 通过次数 0
# # 提交次数 0
# # 题目难度 Easy
# # 泰波那契序列 Tn 定义如下：
# #
# # T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# #
# # 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * 40
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        for i in range(3,n+1):
            memo[i] = memo[i-3] + memo[i-2]+memo[i-1]

        return memo[n]


