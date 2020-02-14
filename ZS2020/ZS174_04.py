# 代码
#
#

# 1340. 跳跃游戏 V  显示英文描述
# 用户通过次数 210
# 用户尝试次数 297
# 通过次数 220
# 提交次数 691
# 题目难度 Hard
# 给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：
#
# i + x ，其中 i + x < arr.length 且 0 < x <= d 。
# i - x ，其中 i - x >= 0 且 0 < x <= d 。
# 除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。
#
# 你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。
#
# 请注意，任何时刻你都不能跳到数组的外面。


# class Solution:
#     def maxJumps(self, arr: List[int], d: int) -> int:
#         def dfs(st):
#             if st in dp:
#                 return dp[st]
#             if st >= len(arr) or st < 0:
#                 return 0
#             ret = 1
#             for i in range(1, d + 1):
#                 if st + i < len(arr) and arr[st + i] < arr[st]:
#                     ret = max(ret, 1 + dfs(st + i))
#                 else:
#                     break
#             for i in range(1, d + 1):
#                 if st - i >= 0 and arr[st - i] < arr[st]:
#                     ret = max(ret, 1 + dfs(st - i))
#                 else:
#                     break
#             dp[st] = ret
#             return ret
#
#         dp = {}
#         ret = 1
#         for i in range(len(arr)):
#             ret = max(ret, dfs(i))
#         return ret