# 905. 按奇偶排序数组

# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        A.sort(key=lambda x:x%2)
        return A

res = Solution().sortArrayByParity([2,3,35,12,2,55])
print(res)

print(2356%2)


dicc = {"d":123,"a":11,"b":2,"c":6}
lis = list(dicc.items())   ##需要转换成list才能有sort方法
print(lis)

lis.sort(key = lambda x:x[0])
print(lis)

lis.sort(key = lambda x:x[1])
print(lis)