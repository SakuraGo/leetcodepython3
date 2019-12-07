# 5034.
# 最大唯一数
# 给你一个整数数组
# A，请找出并返回在该数组中仅出现一次的最大整数。
#
# 如果不存在这个只出现一次的整数，则返回 - 1。
#
# 示例
# 1：
#
# 输入：[5, 7, 3, 9, 4, 9, 8, 3, 1]
# 输出：8
# 解释：
# 数组中最大的整数是
# 9，但它在数组中重复出现了。而第二大的整数是
# 8，它只出现了一次，所以答案是
# 8。

from typing import  List
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        memoDic = {}


        for num in A:
            if num in memoDic.keys():
                memoDic[num] +=1
            else:
                memoDic[num] = 1

        lis =  list(memoDic.items())
        lis.sort(key=lambda x:x[0],reverse=True)
        for num,cnt in lis:

            if cnt == 1:
                return num
        return -1

res = Solution().largestUniqueNumber([5,7,3,9,4,9,8,3,1])
print(res)