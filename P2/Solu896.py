# 896. 单调数列
# 如果数组是单调递增或单调递减的，那么它是单调的。
#
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
#
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。

from typing import List
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        shengxu  = True
        jiangxu = True
        for i in range(1, len(A)):
            chaju = A[i] - A[i-1]
            if chaju>0:
                print("shengxu")
                jiangxu = False

            elif chaju<0:
                print("jiangxu")
                shengxu = False


        return shengxu or jiangxu


Solution().isMonotonic([1,3,2])