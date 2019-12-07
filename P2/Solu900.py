# 900. RLE 迭代器  显示英文描述
# 用户通过次数 108
# 用户尝试次数 151
# 通过次数 111
# 提交次数 480
# 题目难度 Medium
# 编写一个遍历游程编码序列的迭代器。
#
# 迭代器由 RLEIterator(int[] A) 初始化，其中 A 是某个序列的游程编码。更具体地，对于所有偶数 i，A[i] 告诉我们在序列中重复非负整数值 A[i + 1] 的次数。
#
# 迭代器支持一个函数：next(int n)，它耗尽接下来的  n 个元素（n >= 1）并返回以这种方式耗去的最后一个元素。如果没有剩余的元素可供耗尽，则  next 返回 -1 。
#
# 例如，我们以 A = [3,8,0,9,2,5] 开始，这是序列 [8,8,8,5,5] 的游程编码。这是因为该序列可以读作 “三个八，零个九，两个五”。

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

from typing import List
'''
空间复杂度爆炸，内存错误
class RLEIterator:

    def __init__(self, A: List[int]):
        self._cur = []
        for cnt,num in zip(A[::2],A[1::2]):
            self._cur += [num]*cnt
        self._curFlag = 0
    def next(self, n: int) -> int:
        if self._curFlag+n > len(self._cur):
            return -1

        res = self._cur[self._curFlag:self._curFlag+n]
        self._curFlag += n
        return res[-1]
'''

'''
思路：
直接模拟，因为A[i]值较大，所以将[3,8,0,9,2,5]映射成[8,8,8,5,5]存储的方式不可取，会导致内存溢出。
所以应该将A直接存储，每次调用next时候，从数组头部开始检查，如果A[0]小于n，则将A[0]和A[1]移除队列，
并将n自身减去A[0]，直到检查到A[0]大于等于n，记最后被耗去的项是A[1]，并将A[0]减去n。
时间复杂度O(N)O(N)
空间复杂度O(N)O(N)
'''
class RLEIterator:
    def __init__(self, A):
        self.RLE = A

    def next(self, n):
        last = -1
        while self.RLE and self.RLE[0] < n:
            n -= self.RLE[0]
            self.RLE = self.RLE[2:]

        if self.RLE:
            last = self.RLE[1]
            self.RLE[0] -= n
            while self.RLE[0] == 0:
                self.RLE = self.RLE[2:]
        return last



asd = [1,2,3,55]
for innn,nn in enumerate(asd):
    print(innn,nn)
asd += [6]*6
print(asd[::2])