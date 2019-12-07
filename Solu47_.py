# 47. 全排列 II
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

from typing import  List

class Solution:
    def __init__(self):
        self._res = []
        self._used = None

    def bianli(self,nums:List[int],cnt:int,curComs:List[int]):

        if len(curComs) == len(nums):
            print(curComs)
            self._res.append(curComs)
            return

        skipNum = 999999   ##保证统一层级不取相同的数。
        for i in range(len(nums)):
            if nums[i] == skipNum:  ##保证统一层级不取相同的数。
                continue
            if self._used[i] == 1:
                continue
            else:
                self._used[i] = 1
                newLis = curComs.copy()
                newLis.append(nums[i])
                skipNum = nums[i]
                self.bianli(nums,cnt+1,newLis)
                self._used[i] = 0

        return

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<1:
            return self._res

        self._used = [0] * len(nums)
        nums.sort()
        alist = list()
        self.bianli(nums,0,alist)

        return self._res

res =Solution().permuteUnique([1,1,3])
print(res)

