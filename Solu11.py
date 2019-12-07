
# 11. 盛最多水的容器

# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
# 使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
from typing import List

class Solution:

    ##对撞指针式的解决方案
    ##i 和j 比较Height[i] ,Height[j],哪个小，哪个往另一端移动一位
    ##每次都会记下当前的值，与最大值比较
    ##这样的算法是不会漏掉最大值的可能的。。
    ##假设i，j是最大值，面积为s
    ##在i，j+1时刻，错过的条件是Height[i]<Height[j+1],那么最大值就应该是i,j+1... 这是悖论
    def maxArea(self, height: List[int]) -> int:
        maxRes = 0
        l = 0
        r = len(height)-1

        while l<r:

            if height[l] <= height[r]:
                l +=1
            else:
                r -=1

            maxRes = max(maxRes, (r - l) * min(height[l], height[r]))

        return maxRes








# 有问题的解法，漏掉了最大值
#
#     def __init__(self):
#         self._lennn = 0
#         self._l = 0
#         self._r = 0
#         self._prev = 0
#
#     def findLeft(self,heights:List[int]):
#         #r 不动
#         for i in range(self._l+1,self._r):
#             if heights[i]>heights[self._l]:
#                 nowC = min(heights[i],heights[self._r])*(self._r - i)
#                 if nowC > self._prev:
#                     self._l = i
#                     self._prev = nowC
#                     return
#
#         for j in range(0,self._l):
#             nowC = min(heights[j], heights[self._r]) * (self._r - j)
#             if nowC > self._prev:
#                 self._l = j
#                 self._prev = nowC
#                 return
#
#     def findRight(self,heights:List[int]):
#         #l 不dong
#         for i in range(self._r-1,self._l,-1):
#             if heights[i] > heights[self._r]:
#                 nowC = min(heights[i], heights[self._l]) * (i - self._l)
#                 if nowC > self._prev:
#                     self._r = i
#                     self._prev = nowC
#                     return
#
#         for j in range(self._lennn-1, self._r,-1):
#             nowC = min(heights[j], heights[self._l]) * (j - self._l)
#             if nowC > self._prev:
#                 self._r = j
#                 self._prev = nowC
#                 return
#
#
#
#
#     def maxArea(self, height: List[int]) -> int:
#         self._lennn =  len(height)
#         self._l = int(self._lennn/2)-1
#         self._r = int(self._lennn/2)
#         self._prev = min(height[self._l],height[self._r]) * (self._r-self._l)
#         temp = 0
#         while temp != self._prev:
#             print(self._l,self._r)
#             temp = self._prev
#             self.findLeft(height)
#             self.findRight(height)
#
#         return temp
#
# res = Solution().maxArea([2,3,4,5,18,17,6])
#
# print(res)


# sss = [2,3,4,5,6,7,8,9,12]
# for i in range(8,1,-1):
#
#     print(sss[i])
# ll = 9
# a = ll/2
# print(int(a))
