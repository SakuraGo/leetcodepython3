# 529. 扫雷游戏、
#
# 让我们一起来玩扫雷游戏！
#
# 给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。
#
# 现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
#
# 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
# 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
# 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
# 如果在此次点击中，若无更多方块可被揭露，则返回面板。

from typing import List
class Solution:
    def __init__(self):
        self._aa = 0
        self._bb = 0
        self._visited = []

    def isValid(self,y,x):
        return x>=0 and x<self._bb and y>= 0 and y< self._aa



    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        res = board.copy()
        aa= len(board)
        bb = len(board[0])
        self._aa = aa
        self._bb = bb
        print(self._aa,self._bb)
        i,j = click[0],click[1]
        c = board[i][j]
        if c == "M":
            board[i][j] = "X"
            return board

        ## c == "E":
        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        cnt = 0
        for dy,dx in dirs:
            if self.isValid(i+dy,j+dx):
                print(i+dy,j+dx)
                if board[i+dy][j+dx] == "M":
                    cnt += 1
        if cnt > 0:
            board[i][j] = str(cnt)
            return board

        ## cnt 为零，表明需要开始递归遍历展开所有附近没有雷的未揭露的点。
        ## 开始递归遍历
        self._visited = [[0 for j in range(self._bb)] for i in range(self._aa)]

        def dfs(y, x):
            print("y:",y,"x:",x)
            if self.isValid(y, x) is not True:
                return
            cnt = 0
            self._visited[y][x] = 1
            for dy,dx in dirs:
                if self.isValid(y+dy,x+dx):
                    if board[y+dy][x+dx] == "M":
                        cnt += 1
            if cnt > 0:
                board[y][x] = str(cnt)
                return
            else:
                board[y][x] ="B"
                for dy,dx in dirs:
                    if self.isValid(y+dy, x+dx) and self._visited[y+dy][x+dx] == 0:
                        dfs(y+dy,x+dx)
        dfs(i,j)

        return board


res = Solution().updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],[3,0])
print(res)




#
# IndexError: list index out of range
# Line 35 in updateBoard (Solution.py)
# Line 85 in _driver (Solution.py)
# Line 98 in <module> (Solution.py)







