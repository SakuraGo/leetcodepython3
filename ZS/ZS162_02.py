#5256. 重构 2 行二进制矩阵  显示英文描述  我的提交返回竞赛
# # 用户通过次数 161
# # 用户尝试次数 234
# # 通过次数 161
# # 提交次数 420
# # 题目难度 Medium
# # 给你一个 2 行 n 列的二进制数组：
# #
# # 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。
# # 第 0 行的元素之和为 upper。
# # 第 1 行的元素之和为 lower。
# # 第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。
# # 你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。
# #
# # 如果有多个不同的答案，那么任意一个都可以通过本题。
# #
# # 如果不存在符合要求的答案，就请返回一个空的二维数组。
from  typing import List
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        allsum = upper+lower
        if allsum != sum(colsum):
            return []

        res = [[0 for j in range(len(colsum))] for i in range(2)]
        for j in range(len(colsum)):
            if colsum[j] == 2:
                res[0][j] = 1
                res[1][j] = 1
                upper-=1
                lower-=1
        for j in range(len(colsum)):
            if colsum[j] == 1:
                if upper>0:
                    res[0][j] = 1
                    upper-=1
                else:
                    res[1][j] = 1
                    lower -= 1

        print()
        if min(upper,lower)<0:
            return []
        return res

r = Solution().reconstructMatrix(9,2,[0,1,2,0,0,0,0,0,2,1,2,1,2])
print(r)

