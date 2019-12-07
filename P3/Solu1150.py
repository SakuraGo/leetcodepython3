# 1150. 检查一个数是否在数组中占绝大多数
# 给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。假如数组 nums 中绝大多数元素的数值都等于 target，则返回 True，否则请返回 False。
#
# 所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。

from typing import List
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        lenn = len(nums)
        cnt = 0
        for num in nums:
            if num == target:
               cnt += 1

        return cnt > lenn//2


        return True