# 1034. 边框着色

# 给出一个二维整数网格 grid，网格中的每个值表示该位置处的网格块的颜色。
#
# 只有当两个网格块的颜色相同，而且在四个方向中任意一个方向上相邻时，它们属于同一连通分量。
#
# 连通分量的边界是指连通分量中的所有与不在分量中的正方形相邻（四个方向上）的所有正方形，或者在网格的边界上（第一行/列或最后一行/列）的所有正方形。
#
# 给出位于 (r0, c0) 的网格块和颜色 color，使用指定颜色 color 为所给网格块的连通分量的边界进行着色，并返回最终的网格 grid 。
#

# 输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
# 输出：[[3, 3], [3, 2]]

from typing import List
class Solution:

    def __init__(self):
        self._visited = []
        self._aa = 0
        self._bb = 0

    def isValid(self,i,j):
        return  i>=0 and i<self._aa and j >= 0 and j< self._bb

    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        aa = len(grid)
        bb = len(grid[0])
        curColor = grid[r0][c0]
        self._aa = aa
        self._bb = bb

        self._visited = [[0 for j in range(bb)] for i in range(aa)]
        q = list()

        q.append((r0,c0))
        self._visited[r0][c0] = 1

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        while len(q) > 0:
            point = q.pop(0)
            i,j = point

            for k in range(4):
                newi = i + dirs[k][0]
                newj = j + dirs[k][1]


                if self.isValid(newi,newj) is False:  ## 这里到了整个grid的边界，也一定是联通分量的边界。
                    ##出界。。
                    grid[i][j] = color                ##染色这个边界
                    continue
                if self._visited[newi][newj] == 1:
                    continue

                if grid[newi][newj] != curColor:    ##判断 ，这里到了联通分量的边界
                    grid[i][j] = color               ##染色这个边界
                else: ## == curcolor
                    q.append((newi,newj))
                    self._visited[newi][newj] = 1

        return  grid

'''
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        border = set()
        visit = set()

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col and grid[r][c] == grid[r0][c0]):
                return False
            if (r, c) in visit:
                return True
            visit.add((r, c))
            if dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1) < 4:   ##  这里有点意思。。。 有一个边界不与自己同色 即可判定是边界
                border.add((r, c))
            return True

        dfs(r0, c0)
        for (x, y) in border:
            grid[x][y] = color

        return grid
'''














