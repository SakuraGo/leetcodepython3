# 5028.#
# Easy
# 假设存在一个
# k
# 位数
# N，其每一位上的数字的
# k
# 次幂的总和也是
# N，那么这个数是阿姆斯特朗数。
#
# 给你一个正整数
# N，让你来判定他是否是阿姆斯特朗数，是则返回
# true，不是则返回
# false。
#
#
#
# 示例
# 1：
#
# 输入：153
# 输出：true
# 示例：
# 153
# 是一个
# 3
# 位数，且
# 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3。

class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        summm = 0
        for c in str(N):
            summm += int(c) ** k

        return N == summm
