# 303. 区域和检索 - 数组不可变
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。


from typing import  List
'''
##超时！

class NumArray:

    def __init__(self, nums: List[int]):
        self._memo = nums


    def sumRange(self, i: int, j: int) -> int:
        res = 0
        for num in self._memo[i:j+1]:
            res += num
        return res
'''


class NumArray:
    ##使用线段树segmentTree

    def __init__(self, nums: List[int]):
        self._data = nums

        self._segTree = [0] * len(nums)*4
        if len(self._data)<1:
            return
        ##线段树rootindex从1开始计数

        self.buildSegTree(1, 0, len(self._data)-1)

        print(self._segTree)

    def buildSegTree(self,treeIdx,l:int,r:int):
        print(l," ",r)
        if l == r:
            self._segTree[treeIdx] = self._data[l]
            return self._data[l]
        mid = (l+r)//2
        leftIndex = self.leftChild(treeIdx)
        rightIndex = self.rightChild(treeIdx)
        lll = self.buildSegTree(leftIndex,l,mid)
        rrr = self.buildSegTree(rightIndex,mid+1,r)

        self._segTree[treeIdx] = lll+rrr
        return self._segTree[treeIdx]

    ##在 l 到 r 的范围内，寻找 l_pos到r_pos的东西
    def search_segTree(self,treeIdx,l:int,r:int,l_pos,r_pos):
        if l == l_pos and r == r_pos:
            return self._segTree[treeIdx]
        mid = (l+r)//2
        leftChildIdx = self.leftChild(treeIdx)
        rightChildIdx = self.rightChild(treeIdx)

        if r_pos <= mid:
            return self.search_segTree(leftChildIdx,l,mid,l_pos,r_pos)
        if l_pos> mid:
            return self.search_segTree(rightChildIdx,mid+1,r,l_pos,r_pos)
        ##如果都有
        lll = self.search_segTree(leftChildIdx,l,mid,l_pos,mid)
        rrr = self.search_segTree(rightChildIdx,mid+1,r,mid+1,r_pos)
        return lll+rrr

    def leftChild(self,treeIndex):
        return treeIndex*2

    def rightChild(self,treeIndex):
        return treeIndex*2+1

    def sumRange(self, i: int, j: int) -> int:
        if i is None or j is None:
            return 0
        res = self.search_segTree(1, 0, len(self._data)-1,i,j)
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

obj = NumArray([1,2,3,4])
print(obj.sumRange(2,3))


