# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
#
# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
#
# 如果无法让 arr1 严格递增，请返回 -1。
#
#  



print()

'''
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        maxV = 1000000001
        dp = [[maxV for i in range(n+1)] for _ in range(n+1)]

        #initial
        arr2.sort()
        dp[0][0] = -1

        for i in range(1,n+1):
            for j in range(0,i+1):
                if arr1[i-1] > dp[j][i-1]:
                    dp[j][i] = arr1[i-1]

                if j > 0:
                    loc = bisect.bisect_right(arr2,dp[j-1][i-1])
                    if loc < len(arr2):
                        dp[j][i] = min(dp[j][i],arr2[loc])

                if i == n and dp[j][i] != maxV:
                    return j

        return -1


'''