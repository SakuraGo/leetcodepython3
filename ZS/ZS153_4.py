# 1187. 使数组严格递增
# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
#
# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
#
# 如果无法让 arr1 严格递增，请返回 -1。

from typing import List
##超时
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        ###如何构造递推函数。。
        ## dp[i][j] 考虑到 arr1的第i位，且(处理后的)末尾数是j的变换次数

        len1 = len(arr1)
        arr2 = list(set(sorted(arr2)))
        len2 = len(set(arr1)) + len(arr2)
        nums = list(set(sorted(list(set(arr1))+ arr2)))
        print(nums)
        print(arr2)

        dp = [[9999 for j in range(len(nums))] for i in range(len1)]
        # 初始化状态
        for j in range(len(dp[0])):
            if nums[j] == arr1[0]:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        ##递推
        for i in range(1,len(dp)):
            for j in range(i, len(dp[0])):
                mmm = min(dp[i-1][0:j])
                if arr1[i] == nums[j]:  ## 相等
                    dp[i][j] = mmm  ## 从上一个顺序的地方找到。。
                else:
                    if nums[j] in arr2:
                        dp[i][j] = mmm+ 1

        # print(dp)
        return -1 if min(dp[-1])>9000   else min(dp[-1])

        return 1

res = Solution().makeArrayIncreasing([1,5,3,6,7],[1,6,3,3])

print(res)