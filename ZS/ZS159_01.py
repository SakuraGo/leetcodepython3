# 5230. 缀点成线  显示英文描述  我的提交返回竞赛
# 用户通过次数 348
# 用户尝试次数 548
# 通过次数 349
# 提交次数 751
# 题目难度 Easy
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
#
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回true，否则请返回 false
from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #错误的思路
        # if len(coordinates)==2:
        #     return True
        # coordinates = sorted(coordinates,key=lambda  x :x[0])
        # startP = coordinates[0]
        # endP = coordinates[-1]
        # startx,starty = startP[0],startP[1]
        # endx,endy = endP[0],endP[1]
        # chax = (endx-startx) / (len(coordinates)-1)
        # chay =  (endy-starty) / (len(coordinates)-1)
        #
        # curx = startx
        # cury = starty
        # for idx in range(1, len(coordinates)):
        #     point = coordinates[idx]
        #     xx ,yy = point[0],point[1]
        #     if xx == curx+chax and yy == cury + chay:
        #         curx = xx
        #         cury = yy
        #     else:
        #         return False
        #
        # return True
        if len(coordinates)==2:
            return True
        coordinates = sorted(coordinates,key=lambda  x :x[0])
        startP = coordinates[0]
        endP = coordinates[-1]
        startx,starty = startP[0],startP[1]
        endx,endy = endP[0],endP[1]
        chax = (endx-startx)
        chay =  (endy-starty)

        for idx in range(1,len(coordinates)):
            point = coordinates[idx]
            xx ,yy = point[0],point[1]
            if (xx - startx)*chay == (yy-starty)*chax:
                continue
            else:
                return False
        return True

res  = Solution().checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]])
print(res)