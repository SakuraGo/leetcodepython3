# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:


        lenss = len(nums)
        if lenss<1:
            return 0
        if len== 1:
            return nums[0]

        stealMemo = [0] * lenss
        nosMemo = [0] * lenss
        ##偷了第一家
        stealMemo[0] = nums[0]
        nosMemo[1] = 0

        for i in range(1,lenss):
            stealMemo[i] = nosMemo[i-1] + nums[i]
            nosMemo[i] = max(stealMemo[i-1],nosMemo[i-1])
        ##记录第一轮最大值
        s0 = nosMemo[lenss-1]


        ##重置
        stealMemo = [0] * lenss
        nosMemo = [0] * lenss
        ##没偷第一家
        stealMemo[0] = 0
        nosMemo[1] = 0

        for i in range(1,lenss):
            stealMemo[i] = nosMemo[i-1] + nums[i]
            nosMemo[i] = max(stealMemo[i-1],nosMemo[i-1])
        s1 = max(stealMemo[lenss-1],nosMemo[lenss-1])

        return max(s0,s1)

a = 1
b = 2
c = max(a,b)
print(c)