# 1091. 二进制矩阵中的最短路径  显示英文描述
#
# 题目难度 Medium
# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
#
# 一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
#
# 相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
# C_1 位于 (0, 0)（即，值为 grid[0][0]）
# C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
# 如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
# 返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

from typing import List

class Solution:
    def __init__(self):
        self._siz = 0
        self._dirr = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

    def isValid(self,row,column):
        return  (row>= 0 )& (row < self._siz) & (column >= 0 ) & (column < self._siz)


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        self._siz = len(grid)
        num = grid[self._siz-1][self._siz-1]
        if num == 1:
            return -1
        if grid[0][0] == 1:
            return -1
        cur_num = 2
        grid[0][0] = cur_num
        stackLis = [[0,0]]
        while len(stackLis)>0:
            cur_num+=1
            newLis = []
            for pos in stackLis:

                for dirrr in self._dirr:
                    # print(dirrr)
                    new_r = pos[0] + dirrr[0]
                    new_c = pos[1] + dirrr[1]
                    print(new_r, new_c)
                    if (self.isValid(new_r,new_c)) :
                        if (grid[new_r][new_c] == 0):
                            print(cur_num)
                            newLis.append([new_r, new_c])
                            grid[new_r][new_c] = cur_num

            stackLis = newLis
            if len(newLis) == 0:
                break
        if grid[self._siz-1][self._siz-1] == 0:
            return -1
        return grid[self._siz-1][self._siz-1] -1





res  = Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
print(res)
