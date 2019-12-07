# 179. 最大数
# # 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# #
# # 输入: [10,2]
# # 输出: 210
# 输入: [3,30,34,5,9]
# 输出: 9534330
from typing import List



import  functools
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         memo = [[],[]]
#         memo[0].append(3)
#         memo = [13,2,3,56]
#         memo.sort(key= lambda a:a ,reverse=True)
#         print(memo)
#         return 'a'

class Solution(object):
    def sort(self, x, y):
        left, right = x + y, y + x
        return 1 if left > right else -1

    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        if sum(nums) == 0:
            return "0"
        str_list = [str(n) for n in nums]
        str_list.sort(key=functools.cmp_to_key(self.sort), reverse=True)
        return "".join(str_list)

# class Solution(object):
#     def sort(self, x, y):
#         left, right = x + y, y + x
#         return 1 if left > right else -1
#
#     def largestNumber(self, nums):
#         if not nums:
#             return ""
#         if sum(nums) == 0:
#             return "0"
#         str_list = [str(n) for n in nums]
#         str_list.sort(self.sort, reverse=True)
#         return "".join(str_list)

qwer = Solution().largestNumber([3,5,9,97,912,35,8])
print(qwer)
