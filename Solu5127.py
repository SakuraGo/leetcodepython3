# 5127. 数组的相对排序
# 给你两个数组，arr1 和 arr2，
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
from typing import  List

class pair:
    def __init__(self,val,index):
        self._val = val
        self._indx = index

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        memo = []
        for num in arr1:
            if num in arr2:
                memo.append(pair(num,arr2.index(num)))
            else:
                memo.append(pair(num,9999))

        memo.sort(key=lambda x:(x._indx,x._val))
        res= []
        for p in memo:
            res.append(p._val)

        return res

arr = [1,2,3,5,6]
print(arr.index(55))