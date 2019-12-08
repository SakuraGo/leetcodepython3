# 5191. K 次串联后最大子数组之和  显示英文描述
#
# 给你一个整数数组 arr 和一个整数 k。
#
# 首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
#
# 举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
#
# 然后，请你返回修改后的数组中的最大的子数组之和。
#
# 注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
#
# 由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。

from  typing import  List
class Solution:
    def __init__(self):
        self._mod = 1000000000+7

    def maxqujian(self,lis):
        maxxx = 0
        sum = 0
        for num in lis:
            sum += num
            maxxx = max(maxxx, sum)
            if sum < 0:
                sum = 0
        return max(0,maxxx % self._mod)
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k < 3:
            karr = arr * k
            return self.maxqujian(karr)%self._mod

        else:
            allsum = sum(arr)
            karr = arr*2
            maxxx = self.maxqujian(karr)
            if allsum>0:
                return (maxxx + allsum*(k-2))%self._mod
            else:
                return maxxx

res = Solution().kConcatenationMaxSum([-1,-2], 7)

print(res)



qwer = [1,2,3]
karr = qwer * 3
karr[4] = 100
print(karr)