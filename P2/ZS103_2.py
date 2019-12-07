# 909. 蛇梯棋
# 在一块 N x N 的棋盘 board 上，从棋盘的左下角开始，每一行交替方向，按从 1 到 N*N 的数字给方格编号。例如，对于一块 6 x 6 大小的棋盘，可以编号如下：
# 玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。
#
# 每一次从方格 x 起始的移动都由以下部分组成：
#
# 你选择一个目标方块 S，它的编号是 x+1，x+2，x+3，x+4，x+5，或者 x+6，只要这个数字 <= N*N。
# 如果 S 有一个蛇或梯子，你就移动到那个蛇或梯子的目的地。否则，你会移动到 S。
# 在 r 行 c 列上的方格里有 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。
#
# 注意，你每次移动最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。
#
# 返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 -1。

from  typing import  List
class Solution:

    def num2pos(self,num:int,aa:int):
        i = (num-1)//aa
        j = 0
        if i%2 == 0:
            j = (num-1)%aa
        else:
            j = aa-1 -(num-1)%aa
        return j,i

    def pos2num(self,j:int,i:int,aa:int):
        num = 0
        if i %2== 0:
            num = aa*(i) + j + 1
        else:
            num = aa*(i) +1
            num += (aa-1-j)
        return num


    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        steps = [1,2,3,4,5,6]
        aa = len(board)
        visited = [[0 for j in range(aa)] for i in range(aa)]
        que = []
        que.append((0,0,0))  ##存入pos与cnt
        visited[0][0] = 1
        while len(que)>0:
            point = que.pop(0)
            j,i,stepCnt = point
            if i == 5 and j == 1:
                print("qwer")

            oldPoint = self.pos2num(j,i,aa)
            for juli in steps:
                newPoint = oldPoint + juli
                # print("newPoint:",newPoint)
                if newPoint == aa * aa:  ##找到了
                    return stepCnt+1
                if newPoint > aa * aa :
                    continue
                newJ,newI = self.num2pos(newPoint,aa)
                if board[newI][newJ] != -1:
                    if board[newI][newJ] == aa* aa : ##跳到了终点
                        return stepCnt+1
                    newJ,newI = self.num2pos(board[newI][newJ],aa)
                    print("newj:",newJ,"newi:",newI)
                if visited[newI][newJ] == 0:
                    que.append((newJ,newI,stepCnt+1))
                    visited[newI][newJ] = 1
        return -1


res = Solution().snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]])
print(res)