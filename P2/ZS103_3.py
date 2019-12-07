# 910. 最小差值 II  显示英文描述
#
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。
#
# 在此过程之后，我们得到一些数组 B。
#
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

from typing import  List
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        maxxx = max(A)
        minnn = min(A)
        newMin = minnn + K
        print(newMin)
        mayBeMax = 99999
        mayBeMin = -99999
        for index,num in enumerate(A):
            if num < newMin :
                A[index] += K
            elif num> newMin:
                A[index] -= K
            else:
                mayBeMax = num + K
                mayBeMin = num - K
        print(A)
        if mayBeMax == 99999:
            maxx = max(A)
            minn = min(A)
            return maxx - minn
        else:
            res0 = 0
            maxx = max(A)
            minn = min(A)
            maxx = max(maxx,mayBeMax)
            res0 = maxx - minn
            print(res0)
            res1 = 0
            maxx = max(A)
            minn = min(A)
            minn = min(minn,mayBeMin)
            res1 = maxx - minn
            print(res1)
            return min(res0,res1)

        return

res = Solution().smallestRangeII([4,8,2,7,2],5)
print(res)