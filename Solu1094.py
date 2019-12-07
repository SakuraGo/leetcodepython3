# 1094. 拼车  显示英文描述
#
# 题目难度 Medium
# 假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。
#
# 这儿有一份行程计划表 trips[][]，其中 trips[i] = [num_passengers, start_location, end_location] 包含了你的第 i 次行程信息：
#
# 必须接送的乘客数量；
# 乘客的上车地点；
# 以及乘客的下车地点。
# 这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。
#
# 请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所用乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。

# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx = 0
        for trip in trips:
            maxx = max(maxx,trip[-1])

        memo = [0] * (maxx+1)

        for trip in trips:
            startIndex = trip[1]
            endIndex = trip[2]
            weight = trip[0]
            for i in range(startIndex,endIndex):
                memo[i] += weight

        for u in memo:
            print(u)
            if u>capacity:
                return False

        return True


res = Solution().carPooling([[2,1,5],[3,5,7]],3)

