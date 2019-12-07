# 5053. 地图分析


from typing import  List

import queue
###chaoshi
class Solution:

    def __init__(self):
        self._visited = []
        self._aa = 0
        self._queue = queue.Queue()

    def isValid(self,x,y):
        return x>= 0 and x< self._aa and y>=0 and y< self._aa

    def bfs(self,x,y):
        if self.isValid(x,y) is False:
            return

    def maxDistance(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        aa = len(grid)
        self._aa = aa
        iszero = False
        isone = False

        self._visited = [[[0] for i in range(aa)] for j in range(aa)]



        for i in range(aa):
            for j in range(aa):
                if grid[i][j] == 1:
                    isone = True
                    self._queue.put((i,j,0))
                    self._visited[i][j] = 1

                else:
                    iszero = True


        if iszero is False or isone is False:
            return -1

        res = 0
        while self._queue.empty() is False:
            ii,jj,dis = self._queue.get()

            newi,newj = ii,jj,
            newi = ii + dirs[0][0]
            newj = jj + dirs[0][1]
            if self.isValid(newi,newj) is False or self._visited[newi][newj] == 1:
                continue
            else:
                ##处理新的
                self._queue.put((newi,newj,dis+1))
                res = max(res,dis+1)
                self._visited[newi][newj] = 1

            newi,newj = ii,jj,
            newi = ii + dirs[1][0]
            newj = jj + dirs[1][1]
            if self.isValid(newi,newj) is False or self._visited[newi][newj] == 1:
                continue
            else:
                self._queue.put((newi,newj,dis+1))
                res = max(res,dis+1)
                self._visited[newi][newj] = 1

            newi,newj = ii,jj,
            newi = ii + dirs[2][0]
            newj = jj + dirs[2][1]
            if self.isValid(newi,newj) is False or self._visited[newi][newj] == 1:
                continue
            else:
                self._queue.put((newi,newj,dis+1))
                res = max(res,dis+1)
                self._visited[newi][newj] = 1

            newi,newj = ii,jj,
            newi = ii + dirs[3][0]
            newj = jj + dirs[3][1]
            if self.isValid(newi,newj) is False or self._visited[newi][newj] == 1:
                continue
            else:
                self._queue.put((newi,newj,dis+1))
                res = max(res,dis+1)
                self._visited[newi][newj] = 1

        return res

res = Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
print(res)



