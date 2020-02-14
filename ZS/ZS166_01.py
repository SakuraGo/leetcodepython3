# 5279. 整数的各位积和之差  显示英文描述  我的提交返回竞赛
#
# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
#
# 输入：n = 234
# 输出：15
# 解释：
# 各位数之积 = 2 * 3 * 4 = 24
# 各位数之和 = 2 + 3 + 4 = 9
# 结果 = 24 - 9 = 15

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ji = 1
        he = 0
        while n > 0:
            num = n % 10
            ji *= num
            he += num
            n = n // 10

        return ji - he