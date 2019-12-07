# 5215. 黄金矿工  显示英文描述  我的提交返回竞赛
# 题目难度 Medium
# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
#
# 为了使收益最大化，矿工需要按以下规则来开采黄金：
#
# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

# 输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
from  typing import List
class Solution:
    def __init__(self):
        self._row = 0
        self._col = 0
        self._res = 0
        self._visited = []
        self._dirs = []
        self._grid = []

    def isValid(self,r,c):
        return r>= 0 and r< self._row and c>= 0 and c< self._col

    ## 返回当前点之后的dfs金矿值
    def dfsHuiSu(self,r,c,val):
        selVal = self._grid[r][c]
        self._visited[r][c] = 1
        newRes = 0
        for dir in self._dirs:
            deltaR,deltaC = dir
            nr ,nc = r+deltaR,c+deltaC
            if self.isValid(nr,nc) and self._grid[nr][nc]>0 and self._visited[nr][nc] == -1:
                nextVal = self.dfsHuiSu(nr,nc,0)
                newRes = max(newRes,nextVal)
        self._visited[r][c] = -1 ##回溯
        return selVal+newRes


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self._grid = grid
        row = len(grid)
        col = len(grid[0])
        self._row = row
        self._col = col
        self._visited  = [[-1 for j in range(col)] for i in range(row)]
        self._dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] > 0:
                    self._visited  = [[-1 for j in range(col)] for i in range(row)]
                    self._res = max(self._res,self.dfsHuiSu(r,c,0))
                    ## BFS似乎不可取 ，这里要用DFS回溯遍历
                    # que = [(r,c,grid[r][c])]
                    #
                    # while len(que)>0:
                    #     rr,cc,val = que.pop(0)
                    #     self._res = max(self._res,val)
                    #     for dir in dirs:
                    #         deltaR,deltaC = dir
                    #         nr = rr+deltaR
                    #         nc = cc+deltaC
                    #         if self.isValid(nr,nc) and grid[nr][nc]>0 and visited[nr][nc] == -1:
                    #             que.append((nr,nc,val+grid[nr][nc]))
                    #             visited[nr][nc] = 1
                    #         else:
                    #             continue



        return self._res


















