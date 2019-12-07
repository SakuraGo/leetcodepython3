# 5113. 删除区间  显示英文描述  我的提交返回竞赛
# 用户通过次数 29
# 用户尝试次数 36
# 通过次数 29
# 提交次数 48
# 题目难度 Medium
# 给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[i] = [a, b] 都表示满足 a <= x < b 的所有实数  x 的集合。
#
# 我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。
#
# 返回删除所有交集区间后， intervals 剩余部分的 有序 列表
from  typing import  List
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        minn = toBeRemoved[0]
        maxx = toBeRemoved[1]
        res = []
        for interval in intervals:
            if interval[1]<=minn:
                res.append(interval)
                continue
            if interval[0]>= maxx:
                res.append(interval)
                continue
            if interval[0]>= minn and interval[1] <= maxx:
                continue
            if interval[1]<=maxx:
                res.append([interval[0],minn])
                continue
            if interval[0]>=minn:
                res.append([maxx,interval[1]])
                continue
            if interval[0]<=minn and interval[1] >= maxx:
                res.append([interval[0],minn])
                res.append([maxx,interval[1]])

        return res