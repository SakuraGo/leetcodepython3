# 78. 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from typing import List


class Solution:

    def __init__(self):
        self._res = []

    def combinNums(self,cur: List[int],leftNums:List[int]):
        if len(leftNums) == 0:
            self._res.append(cur)
            print(cur)
            return
        num = leftNums[0]
        cur0 = cur.copy()
        cur.append(num)

        self.combinNums(cur0,leftNums[1:])
        self.combinNums(cur,leftNums[1:])

    def subsets(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return self._res
        ccc = []
        self.combinNums(ccc,nums)
        return self._res

res = Solution().subsets([1,2,3])

ccb = []
ccb.append(3)
ccb.append(35)
print(ccb)