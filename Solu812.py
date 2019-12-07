# 812. 最大三角形面积

# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

from typing import List
class Solution:
    def mianji(self,threePoints):
        one,two,three = threePoints
        x1,y1  = one[0],one[1]
        x2,y2 = two[0],two[1]
        x3,y3 = three[0],three[1]
        # print((x1*y2+x2*y3+x3*y1-x1*y3 - x2*y1 - x3*y2)/2)
        return (x1*y2+x2*y3+x3*y1-x1*y3 - x2*y1 - x3*y2)/2


    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for firstIdx in range(0, len(points)-2):
            for twoIdx in range(firstIdx+1,len(points)-1):
                for threeIdx in range(twoIdx+1,len(points)):
                    mianji = self.mianji([points[firstIdx],points[twoIdx],points[threeIdx]])
                    print(mianji)
                    res  = max(res,abs(mianji))

        return res

res  = Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
print(res)

print(Solution().mianji([[0,0],[2,0],[0,2]]))