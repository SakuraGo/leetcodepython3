# 5136. 矩形内船只的数目  显示英文描述  我的提交返回竞赛
# 用户通过次数 27
# 用户尝试次数 36
# 通过次数 27
# 提交次数 44
# 题目难度 Hard
# (此题是 交互式问题 )
#
# 在用笛卡尔坐标系表示的二维海平面上，有一些船。每一艘船都在一个整数点上，且每一个整数点最多只有 1 艘船。
#
# 有一个函数 Sea.hasShips(topRight, bottomLeft) ，输入参数为右上角和左下角两个点的坐标，当且仅当这两个点所表示的矩形区域（包含边界）内至少有一艘船时，这个函数才返回 true ，否则返回 false 。
#
# 给你矩形的右上角 topRight 和左下角 bottomLeft 的坐标，请你返回此矩形内船只的数目。题目保证矩形内 至多只有 10 艘船。
#
# 调用函数 hasShips 超过400次 的提交将被判为 错误答案（Wrong Answer） 。同时，任何尝试绕过评测系统的行为都将被取消比赛资格。

from  typing import  List

class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       return True
#
class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y
        # self._sea = 0


class Solution(object):
    def __init__(self):
        self._cnt = 0
        self._tenFlag = False
        self._sea = None
        self._memo = []

    def digui(self, topRight: 'Point', bottemLeft: 'Point'):
        # if self._tenFlag is True:

        if topRight.x == bottemLeft.x and topRight.y == bottemLeft.y :
            if  self._sea.hasShips(topRight, bottemLeft):
                if [topRight.x,topRight.y] in self._memo:
                    return
                self._cnt += 1
                self._memo.append([topRight.x,topRight.y])
                print(topRight.x, topRight.y, bottemLeft.x, bottemLeft.y)
                if self._cnt >= 10:
                    self._tenFlag = True
                return
            else:
                return

        print("----:", topRight.x, topRight.y, bottemLeft.x, bottemLeft.y)
        if self._sea.hasShips(topRight, bottemLeft) is False:
            return
        else:
            hx = bottemLeft.x + (topRight.x - bottemLeft.x) // 2
            hy = bottemLeft.y + (topRight.y - bottemLeft.y) // 2
            # newPoint0 = Point(bottemLeft,)
            self.digui(Point(hx, hy), bottemLeft)
            self.digui(Point(topRight.x, hy), Point(min(hx + 1,topRight.x), bottemLeft.y))
            self.digui(Point(hx, topRight.y), Point(bottemLeft.x, min(hy + 1,topRight.y)))
            self.digui(topRight, Point(min(hx + 1,topRight.x), min(hy + 1,topRight.y)))

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        self._sea = sea
        x0, y0 = bottomLeft.x, bottomLeft.y
        x1, y1 = topRight.x, topRight.y

        self.digui(topRight, bottomLeft)
        return self._cnt


