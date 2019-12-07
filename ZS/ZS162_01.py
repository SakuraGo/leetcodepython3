# 5255. 奇数值单元格的数目  显示英文描述  我的提交返回竞赛
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Easy
# 给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。
#
# 另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
#
# 你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。
#
# 请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

from typing import  List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0 for row in range(n)]
        cols = [0 for col in range(m)]
        for ind in indices:
            r ,c = ind[0],ind[1]
            rows[r] = int (not rows[r])
            cols[c] = int (not cols[c])

        sumRow = sum(rows)
        sumCol = sum(cols)
        return sumRow*m + sumCol*n - sumRow*sumCol*2

res  = Solution().oddCells(2,2,[[1,1],[0,0]])
print(res)