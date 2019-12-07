# 5073. 进击的骑士  显示英文描述  我的提交返回竞赛
#
# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。
#
# 骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格。
#
# 每次移动，他都可以按图示八个方向之一前进。

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        x = abs(x)
        y = abs(y)
        visited = [[0 for j in range(x+3)] for i in range(y+3)]
        dirs = [(1,2),(2,1),(-1,2),(2,-1),(-1,-2),(-2,-1),(1,-2),(-2,1)]
        targetx= x+1
        targety = y+1
        print(targetx,targety)
        def isValid(x,y):
            return x >= 0 and y >= 0 and x < len(visited[0]) and y < len(visited)

        qqq = [(1,1,0)]  ## x,y,stepCnt
        visited[1][1] = 1
        ##bfs思路
        while len(qqq) > 0:
            curPoint = qqq.pop(0)
            x,y,curStep = curPoint
            print(x,y,curStep)
            for dir in dirs:
                dx,dy = dir
                newx = x+dx
                newy = y+dy
                if isValid(newx,newy) is False:
                    continue
                ##下面是有效的点
                # if newx == 3 and newy == 2:
                #     print("q")
                if newx == targetx and newy == targety: ##找到了！
                    return curStep+1
                else:
                    if visited[newy][newx] == 1:
                        continue
                    else:
                        visited[newy][newx] = 1
                        qqq.append((newx,newy,curStep+1))


res = Solution().minKnightMoves(2,1)
print(res)




