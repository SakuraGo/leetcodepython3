# 695. 岛屿的最大面积
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

from typing import List

class Solution:
    def __init__(self):
        self._maxx = 0
        self._visited = []
        self._aa = 0
        self._bb = 0
        self._dirr =  [[1,0],[-1,0],[0,1],[0,-1]]
        self._g = None

    def isValidPoint(self,i:int , j:int):
        return i>=0 and i<self._aa and j>=0 and j<self._bb and self._g[i][j] == 1

    def dfsGrid(self,i:int ,j:int): #遍历grid，返回以（i，j）为起始点dfs的所遍历到的节点总数
        self._visited[i][j] = 1
        sum = 0
        for deltai,deltaj in self._dirr:

            if self.isValidPoint(i + deltai, j + deltaj) :
                if self._visited[i+deltai][j+deltaj] == 1: #已访问过的点
                    print("已访问过--",i+deltai,j+deltaj)
                else: #未访问过的点
                    sum += self.dfsGrid(i+deltai,j+deltaj)
        return sum+1


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        aa= len(grid)
        bb = len(grid[0])
        self._aa = aa
        self._bb = bb
        self._g = grid
        if aa == 0 or bb== 0:
            return self._maxx

        self._visited = [None] * aa
        for i in range(aa):
            lis = [0] * bb
            self._visited[i] = lis

        for i in range(aa):
            for j in range(bb):
                if grid[i][j] == 0:
                    continue
                else:
                    if self._visited[i][j] == 0: ## 找到了1 ，且未访问过，开始dfs遍历
                        res = self.dfsGrid(i,j)
                        self._maxx = max(self._maxx,res)

        return self._maxx


res = Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])

print(res)