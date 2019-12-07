# 1095.
# 山脉数组中查找目标值
#
# 给你一个
# 山脉数组
# mountainArr，请你返回能够使得
# mountainArr.get(index)
# 等于
# target
# 最小
# 的下标
# index
# 值。
#
# 如果不存在这样的下标
# index，就请返回 - 1。
#
#
#
# 所谓山脉数组，即数组
# A
# 假如是一个山脉数组的话，需要满足如下条件：
#
# 首先，A.length >= 3
#
# 其次，在
# 0 < i < A.length - 1
# 条件下，存在
# i
# 使得：
#
# A[0] < A[1] < ...
# A[i - 1] < A[i]
# A[i] > A[i + 1] > ... > A[A.length - 1]
#
# 你将
# 不能直接访问该山脉数组，必须通过
# MountainArray
# 接口来获取数据：
#
# MountainArray.get(k) - 会返回数组中索引为k
# 的元素（下标从
# 0
# 开始）
# MountainArray.length() - 会返回该数组的长度
#
# 注意：
#
# 对
# MountainArray.get
# 发起超过
# 100
# 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。
#
# 为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https: // leetcode - cn.com / playground / RKhe3ave，请注意这
# 不是一个正确答案

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int: return 1
   def length(self) -> int:return 2


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        return 1

asd = 9//2
print(asd)

'''
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 1, n-2
        while left < right:
            mid = (left+right)//2
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                right = mid
            else:
                left = mid+1
        top = left
        left, right = 0, top
        while left <= right:
            mid = (left+right)//2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                right = mid - 1
            else:
                left = mid + 1
        left, right = top, n-1
        while left <= right:
            mid = (left+right)//2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
'''