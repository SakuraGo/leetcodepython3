# 5250. 检查「好数组」  显示英文描述  我的提交返回竞赛
# 用户通过次数 137
# 用户尝试次数 191
# 通过次数 144
# 提交次数 378
# 题目难度 Hard
# 给你一个正整数数组 nums，你需要从中任选一些子集，然后将子集中每一个数乘以一个 任意整数，并求出他们的和。
#
# 假如该和结果为 1，那么原数组就是一个「好数组」，则返回 True；否则请返回 False。

# 输入：nums = [12,5,7,23]
# 输出：true
# 解释：挑选数字 5 和 7。
# 5*3 + 7*(-2) = 1
from typing import List
class Solution:

    ## 求最小公约数
    def lcd(self,x, y):
        if y == 0:
            return x
        else:
            return self.lcd(y, x % y)

    def isGoodArray(self, nums: List[int]) -> bool:
        if 1 in nums:
            return True
        if len(nums)<2:
            return False
        # print(self.lcd(18,15))
        flag = False
        nums = sorted(nums)
        gongyushu = self.lcd(nums[0],nums[1])
        if gongyushu== 1:
            return True
        for idx,num in enumerate(nums):
            if idx<=1:
                continue
            else:
                gongyushu = self.lcd(gongyushu,num)
                if gongyushu == 1:
                    return True

        return False

res = Solution().isGoodArray([999999999,999999997])
print(res)