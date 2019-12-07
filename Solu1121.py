# 1121. 将数组分成几个递增序列
# 输入：nums = [1,2,2,3,3,4,4], K = 3
# 输出：true
# 解释：
# 该数组可以分成两个子序列 [1,2,3,4] 和 [2,3,4]，每个子序列的长度都至少是 3。

from typing import List
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        memoDic = {}
        lenn = len(nums)
        maxCnt = 0
        for num in nums:
            if num in memoDic.keys():
                memoDic[num] +=1
                maxCnt = max(maxCnt,memoDic[num])
            else:
                memoDic[num] = 1

        if maxCnt * K <= lenn:
            return True
        else:
            return False



