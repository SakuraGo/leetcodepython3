# 1151. 最少交换次数来组合所有的 1
# 给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

from  typing import List
class Solution:
    def __init__(self):
        self._memo = [0] ##前n个数之和
    def minSwaps(self, data: List[int]) -> int:
        sum = 0
        for num in data:
            sum += num
            self._memo .append(sum)

        lenn = sum

        minn = 999999

        l = 0
        r = l + lenn - 1
        while (r < len(data)):
            curSum = self._memo[r+1] - self._memo[l]
            minn = min(minn,sum - curSum)
            l+= 1
            r+= 1

        return minn




