# 16. 最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
from typing import  List
class Solution:
    def __init__(self):
        self._memo = {}

    def searchBias(self,bias:int,target:int,nums:List[int]):
        newTarget = target+bias
        for i in range(len(nums)):
            for k,v in self._memo.items():
                if k == newTarget - nums[i]:
                    for comp in v:
                        if i not in comp:
                            return True,bias
        return False,bias

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<4:
            return sum(nums)
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] in self._memo.keys():
                    self._memo[nums[i]+nums[j]].append([i,j])
                else:
                    self._memo[nums[i]+nums[j]] = [[i,j]]

        bias0 = 0
        bias1 = 0
        while (1):
            flag,bias = self.searchBias(bias0,target,nums)
            if flag is True:
                return bias+target

            flag, bias = self.searchBias(bias1, target, nums)
            if flag is True:
                return bias+target
            bias0 +=1
            bias1 -=1

        return 1


res = Solution().threeSumClosest([-1,2,1,-4],1)
print(res)
# dic = {3:5}
# for v in dic.values():
#     print(dic)
#     print(v)

