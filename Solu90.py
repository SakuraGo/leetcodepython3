# 90. 子集 II
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
from typing import List


class Solution:
    def __init__(self):
        self._res = [[]]

    def huisuo(self, numss: List[int], curIndex: int, curCom: List[int]):
        if curIndex == len(numss) - 1:
            cur0 = curCom.copy()
            cur1 = curCom.copy()
            cur0.append(numss[curIndex])
            if cur0 not in self._res:
                self._res.append(cur0)
            if cur1 not in self._res:
                self._res.append(cur1)
            return
        # if curIndex >= len(numss):
        #     return

        pre = -939
        for j in range(curIndex, len(numss)):
            if (numss[j] == pre)&(j != curIndex):
                print("tiao")
                continue
            # c0 = curCom.copy()
            # c1 = curCom.copy()
            curCom.append(numss[j])
            self.huisuo(numss, j + 1, curCom)
            curCom.pop()
            self.huisuo(numss, j + 1, curCom)

            # print(qq)
            # self.huisuo(numss,j+1,curCom)
            pre = numss[j]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<1:
            return [[]]
        nums = sorted(nums)
        self.huisuo(nums, 0, [])

        return self._res









    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.huisuo(nums,0,[])



        return self._res

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      
    # dfs
    
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)  ## 求子集的话，在此处即可插入res...
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)
'''