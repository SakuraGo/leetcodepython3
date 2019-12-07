# 5088. 等差数列中缺失的数字  显示英文描述  我的提交返回竞赛
#
# 数组 arr 中的值符合等差数列的数值规律：在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。
#
# 然后，我们从数组中删去一个 既不是第一个也不是最后一个的值 。
#
# 给你一个缺失值的数组，请你帮忙找出那个被删去的数字。
# 输入：arr = [5,7,11,13]
# 输出：9
# 解释：原来的数组是 [5,7,9,11,13]。
from typing import List
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[-1] == arr[0]:
            return arr[0]
        cha = (arr[-1] - arr[0]) / len(arr)
        cur = arr[0]
        for num in arr:
            if num != cur:
                return int(cur)
            else:
                cur += cha
