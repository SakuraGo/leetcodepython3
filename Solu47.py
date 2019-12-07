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


    def bianli(self,nums:List[int],cnt:int,curComp:List[int]):
        print("a")
        if curComp and len(curComp) == len(nums):
            if curComp in self._res:
                return
            else:
                self._res.append(curComp)
                return

        for i in range(len(nums)):
            if self._used[i] == 0:
                self._used[i] = 1
                newLis = curComp.copy()
                newLis.append(nums[i])
                self.bianli(nums,cnt+1,newLis)
                self._used[i] = 0

            else:
                continue
        return



    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # print("asdf")

        if len(nums) < 1:
            return self._res

        self._used = [0] * len(nums)
        aLis = list()
        self.bianli(nums,0,aLis)

        return self._res



asd = [[1,2],[2,3]]
print([1,3] in asd)

ress = Solution().permuteUnique([1,1,3])
print(ress)