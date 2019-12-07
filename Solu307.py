# 307. 区域和检索 - 数组可修改

# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8


from typing import List
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

    def update(self, i: int, val: int) -> None:
        self._data[i] = val
        self.updateTree(1, 0, len(self._data)-1,i,val)

    def updateTree(self,treeIdx,l,r,index,val):
        if l== r:
            self._segTree[treeIdx] = val
            return val

        mid = (l+r)//2
        leftChildIdx = self.leftChild(treeIdx)
        rightChildIdx = self.rightChild(treeIdx)
        if index<= mid:
            newTree =  self.updateTree(leftChildIdx,l,mid,index,val)
            self._segTree[treeIdx] = newTree + self._segTree[rightChildIdx]
            return self._segTree[treeIdx]

        if index>mid:
            newTree = self.updateTree(rightChildIdx,mid+1,r,index,val)
            self._segTree[treeIdx] = newTree + self._segTree[leftChildIdx]
            return self._segTree[treeIdx]


    def leftChild(self,treeIndex):
        return treeIndex*2

    def rightChild(self,treeIndex):
        return treeIndex*2+1

    def sumRange(self, i: int, j: int) -> int:
        if i is None or j is None:
            return 0
        res = self.search_segTree(1, 0, len(self._data)-1,i,j)
        return res

obj = NumArray([1,3,5])
print(obj.sumRange(0,2))
obj.update(1,2)
print(obj.sumRange(0,2))