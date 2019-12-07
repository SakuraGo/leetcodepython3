# 机器人大冒险  显示英文描述  我的提交
# 用户通过次数 79
# 用户尝试次数 407
# 通过次数 79
# 提交次数 831
# 题目难度 Medium
# 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：
#
# U: 向y轴正方向移动一格
# R: 向x轴正方向移动一格。
# 不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。
#
# 给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

from  typing import List
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        ucnt = 0
        rcnt = 0
        for c in command:
            if c == "U":
                ucnt += 1
            elif c == "R":
                rcnt += 1
        newx = x % rcnt
        newy = y % ucnt

        matrix = [[0 for j in range(rcnt+1)] for i in range(ucnt+1)]

        def getobs(x,y):
            xx = x // rcnt
            yy = y // ucnt
            dd = min(xx,yy)
            nx = x- dd * rcnt
            ny = y- dd * ucnt
            return [nx,ny]

        # newobstac = []
        for ox,oy in obstacles:
            print("ox,oy:",ox,oy)
            if ox>x or oy > y :
                continue
            xx,yy = getobs(ox,oy)
            if xx > rcnt or yy > ucnt:
                continue
            else:
                # newobstac.append([xx,yy])
                matrix[ucnt-yy][xx] = -1

        print(matrix)
        newx,newy = getobs(x,y)
        if newx>rcnt or newy > ucnt :
            return False
        else:
            matrix[ucnt-newy][newx] = 1
        pos = [0,0]
        touchFlag = False
        for c in command:
            if c == "U":
                pos[1] += 1
            else:
                pos[0] += 1

            if matrix[ucnt-pos[1]][pos[0]] == -1:
                return False
            elif matrix[ucnt-pos[1]][pos[0]] == 1:
                touchFlag = True
        if touchFlag is True:
            return True
        else:
            return False
        # return True

res = Solution().robot("URR",[[4, 2]], x = 3, y = 2)
print(res)

'''
代码
class Solution:
    def robot(self, command: str, ob: List[List[int]], sx: int, sy: int) -> bool:
        n = command.count('R')
        m = command.count('U')
        x = y = 0
        vo = vs = False
        for ch in command:
            if ch == 'R':
                x += 1
            else:
                y += 1
            if (x, y) == (sx, sy):
                return True
            if (sx - x) % n == 0 and (sy - y) % m == 0 and (sx - x) // n == (sy - y) // m:
                vs = True
            for ox, oy in ob:
                if (x, y) == (ox, oy):
                    return False
                if ox <= sx and oy <= sy:
                    if (ox - x) % n == 0 and (oy - y) % m == 0 and (ox - x) // n == (oy - y) // m:
                        vo = True
        return not vo and vs
'''
