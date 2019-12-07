# 5181. 公交站间的距离
# 环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。
#
# 环线上的公交车都可以按顺时针和逆时针的方向行驶。
#
# 返回乘客从出发点 start 到目的地 destination 之间的最短距离。

from typing import  List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start== destination:
            return 0
        mins = min(start,destination)
        maxs = max(start,destination)
        summ = sum(distance)
        partSum = 0
        for i in range(mins,maxs):
            partSum += distance[i]

        return min(partSum,summ-partSum)

