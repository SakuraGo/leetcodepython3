# 5208. 穿过迷宫的最少移动次数  显示英文描述
# 用户通过次数 13
# 用户尝试次数 22
# 通过次数 14
# 提交次数 32
# 题目难度 Hard
# 你还记得那条风靡全球的贪吃蛇吗？
#
# 我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。
#
# 每次移动，蛇可以这样走：
#
# 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
# 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
# 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

from  typing import  List

class Solution:
    def __init__(self):
        self._R = 0
        self._C = 0
    def minimumMoves(self, grid: List[List[int]]) -> int:
        ## 思路是进行bfs..

        self._R = len(grid)
        self._C = len(grid[0])
        endSnake = ((self._R-1,self._C-2),(self._R-1,self._C-1))
        def isValid(r,c):
            return r>= 0 and r<self._R and c>= 0 and c< self._C

        startSnake = ((0,0),(0,1),0)
        dirs = [((0,1),(0,1)),((1,0),(1,0)),((0,0),(1,-1)),((0,0),(-1,1))]

        memoSet = set()
        memoSet.add(((0,0),(0,1)))
        q = [startSnake]

        while len(q)>0:
            curSnake = q.pop(0)
            p0 = curSnake[0]
            p1 = curSnake[1]
            step = curSnake[2]
            p0i = p0[0]
            p0j = p0[1]
            p1i = p1[0]
            p1j = p1[1]


            for dir in dirs:
                if p0j == p1j and dir == ((0,0),(1,-1)):
                    # print("左翻..")
                    continue
                if p0i == p1i and dir == ((0,0),(-1,1)):
                    # print("上翻..")
                    continue
                if dir == ((0,0),(1,-1)) or dir == ((0,0),(-1,1)):
                    if isValid(p0i+1,p0j+1)  and grid[p0i+1][p0j+1] == 1:
                        continue


                newp0i = p0i +dir[0][0]
                newp0j = p0j + dir[0][1]
                newp1i = p1i +dir[1][0]
                newp1j = p1j + dir[1][1]

                if isValid(newp0i,newp0j) and isValid(newp1i,newp1j):
                    # print()
                    newSnake = (newp0i,newp0j),(newp1i,newp1j)
                    if newSnake == endSnake:
                        return step+1
                    if (newSnake) not in memoSet:
                        if grid[newp0i][newp0j] == 0 and grid[newp1i][newp1j] == 0:
                            memoSet.add(newSnake)
                            q.append(((newp0i,newp0j),(newp1i,newp1j),step+1))

        return -1


# startPoint = ((0, 0), (0, 1))
# endP =  ((0, 0), (0, 1))
# print(startPoint == endP)
# mmset = set()
# mmset.add(startPoint)
# print(endP in  mmset)
res  = Solution().minimumMoves([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,1,0,0,1,0,0,0,0,1,0,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,0]])
print(res)

liss = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,1,0,0,1,0,0,0,0,1,0,0],[0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,0]]
for lis in liss:
    print(lis)
