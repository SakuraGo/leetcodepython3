# 5079. 三个有序数组的交集
# 给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。
#
# 返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。
from typing import List
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = set()
        res = res | set(arr1)
        res = res & set(arr2)
        res = res & set(arr3)
        print(res)
        ress = sorted(list(res))
        # print(ress)
        return ress

res  = Solution().arraysIntersection([1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8])
print(res)