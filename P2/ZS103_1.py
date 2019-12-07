# 908. 最小差值 I  显示英文描述
#
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
#
# 在此过程之后，我们得到一些数组 B。
#
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

from typing import List
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxxx = max(A)
        minnn = min(A)
        res = maxxx-minnn - 2*K
        return maxxx-minnn - 2*K if res>0 else 0  ## 从原来的里面挑最大的看能减到多小，以及最小的看能加到多大。。