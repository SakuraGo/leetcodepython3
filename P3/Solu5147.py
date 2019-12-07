# 5147. 递减元素使数组呈锯齿状
# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
#
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
#
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。

from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        minnn = 9999999
        cnt = 0
        ##"M"
        for index in range(0, len(nums),2):

            mountainMin = 1010
            if index!= 0 and index!= len(nums)-1:
                mountainMin = min(mountainMin,nums[index-1])
                mountainMin = min(mountainMin,nums[index+1])

            if index == 0:
                mountainMin = min(mountainMin,nums[index+1])

            if index == len(nums) - 1:
                mountainMin  = min(mountainMin,nums[index-1])

            if nums[index]> mountainMin-1:
                 cnt += (nums[index] - mountainMin + 1)

        minnn = min(minnn,cnt)

        ##"W"
        cnt = 0

        for index in range(1, len(nums),2):
            mountainMin = 1010
            if index!= len(nums) - 1:
                mountainMin = min(mountainMin, nums[index - 1])
                mountainMin = min(mountainMin, nums[index + 1])
            elif index == len(nums) - 1:
                mountainMin = min(mountainMin, nums[index - 1])

            if nums[index]> mountainMin-1:
                 cnt += (nums[index] - mountainMin + 1)

        minnn = min(minnn, cnt)


        return minnn


res = Solution().movesToMakeZigzag([151,42,769,349,835,92,242,82,357,494,880,683,470,631,479,298,941,113,892,103,755,575,885,50,479,502,181,164,292,832,657,512,528,588,716,965,195,106,396,649])
print(res)

print(len(
    [151, 42, 769, 349, 835, 92, 242, 82, 357, 494, 880, 683, 470, 631, 479, 298, 941, 113, 892, 103, 755, 575, 885, 50, 479, 502, 181, 164, 292, 832, 657, 512, 528, 588, 716, 965, 195, 106, 396, 649]))