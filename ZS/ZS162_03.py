# 5257. 统计封闭岛屿的数目  显示英文描述  我的提交返回竞赛
# 用户通过次数 138
# 用户尝试次数 168
# 通过次数 138
# 提交次数 194
# 题目难度 Medium
# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
#
# 我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
#
# 如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
#
# 请返回封闭岛屿的数目。
from  typing import List
class Solution:
    def __init__(self):
        self._r = 0
        self._c = 0

    def isValid(self,row,col):
        return row>=0 and row < self._r and col>=0 and col<self._c

    def isEdge(self,row,col):
        return row==0 or col == 0 or row == (self._r-1) or col == (self._c-1)

    def closedIsland(self, grid: List[List[int]]) -> int:
        ##
        self._r = len(grid)
        self._c = len(grid[0])
        res = 0
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:##水域
                    continue
                print("r,c", row, col)
                islandFlag = True
                if visited[row][col] == 1:
                    continue
                if visited[row][col] == 0:
                    res += 1 ##先不管什么情况加一个
                    ## bfs
                    q = [(row,col)] ##里边的东西一定是有效的

                    while len(q)>0:

                        point = q.pop(0)
                        r,c = point
                        visited[r][c] = 1
                        if self.isEdge(r,c):
                            islandFlag = False ##不是岛屿

                        for dir in dirs:
                            nr = r+dir[0]
                            nc = c+dir[1]
                            if self.isValid(nr,nc) and visited[nr][nc] == 0 and grid[nr][nc]==0:
                                q.append((nr,nc))
                                visited[nr][nc] = 1
                if islandFlag is False:
                    res-=1
        return res


asd = Solution().closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])
print(asd)




