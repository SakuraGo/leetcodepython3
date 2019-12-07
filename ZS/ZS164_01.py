# 5271. 访问所有点的最小时间  显示英文描述  我的提交返回竞赛
# 用户通过次数 635
# 用户尝试次数 676
# 通过次数 641
# 提交次数 737
# 题目难度 Easy
# 平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。
#
# 你可以按照下面的规则在平面上移动：
#
# 每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
# 必须按照数组中出现的顺序来访问这些点。
from typing import  List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        cur = points[0]
        x,y = cur[0],cur[1]
        for idx,point in enumerate(points):
            if idx == 0:
                continue

            nx,ny = point[0],point[1]
            chax = abs(nx-x)
            chay = abs(ny-y)
            res += max(chax,chay)
            x,y = nx,ny

        return  res
