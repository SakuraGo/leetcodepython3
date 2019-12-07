from typing import  List
class Solution:
    def __init__(self):
        self._visited = [0]
        self._aa = 0

    def maxDistance(self, grid: List[List[int]]) -> int:
        aa = len(grid)
        self._aa = aa
        self._visited = [[0 for i in range(aa)] for j in range(aa)]


        lis = list()
        for i in range(aa):
            for j in range(aa):
                if grid[i][j] == 1:
                    self._visited[i][j] = 1
                    lis.append((i,j,0))

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        res = 0
        while lis:
            point = lis.pop(0)
            x,y,dis = point

            for bi,bj in dirs:
                newx = x + bi
                newy = y + bj

                if 0<= newx    < self._aa and 0<= newy < self._aa and self._visited[newx][newy] == 0:
                    lis.append((newx,newy,dis+1))
                    self._visited[newx][newy] = 1
                    res = max(res,dis+1)

        return res if res != 0 else -1


lis = list()
lis.append(1)
lis.append(31)
lis.append(2)

print(lis)
lis.pop(0)
print(lis)

_visited = [[0 for i in range(5)] for j in range(5)]
print(_visited)
