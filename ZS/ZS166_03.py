# 5281. 使结果不超过阈值的最小除数  显示英文描述  我的提交返回竞赛
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Medium
# 给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
#
# 请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
#
# 每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
#
# 题目保证一定有解。

# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。

from  typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = threshold
        # maxxx = 9999999999999
        # for n in range(threshold,0,-1):
        #     jieguo = 0
        #     for num in nums:
        #         xiaoshu =  num % n
        #         if xiaoshu>0:
        #             jieguo = jieguo + num//n + 1
        #         else:
        #             jieguo = jieguo + num//n
        #     print(jieguo,n)
        #     if jieguo<maxxx:
        #         res = n
        #         maxxx = jieguo
        # return res

        ##读错题目 ，从小到大算
        ## 二分法思路
        l = 1
        r = max(nums)
        while l<r:
            mid = (l+r)//2
            jieguo = 0
            for num in nums:
                xiaoshu = num % mid
                if xiaoshu>0:
                    jieguo = jieguo+ num//mid+1
                else:
                    jieguo = jieguo + num//mid
            if jieguo<=threshold:
                r = mid
            else:
                l = max(l+1,mid)
        return (l+r)//2



qw = Solution().smallestDivisor([2,3,5,7,11],11)
print(qw)
