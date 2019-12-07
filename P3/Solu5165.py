# 5165. 餐盘栈
# 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。
#
# 实现一个叫「餐盘」的类 DinnerPlates：
#
# DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
# void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
# int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
# int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
# add
from heapq import *


'''
work but timeout
'''
class DinnerPlates:

    def __init__(self, capacity: int):
        self._capacity = capacity
        # self._numOfStack = 0
        self._notFull = set()  ## 记录没有满编的stack 的index，
        self._memo = []  ##存储数据
        self._stackCnt = {}   ## 每个stack的个数
    def push(self, val: int) -> None:
        if val<= 0 :
            return
        ## 从notfull中找一个最小的push  ，如果都满了就新建一个组
        if len(self._notFull)>0:
            heapify(list(self._notFull))
            temp = self._notFull.copy()
            index = heappop(list(temp))
            tempStack = self._memo[self._capacity * index:self._capacity * (index + 1)]
            tempStack[self._stackCnt[index]] = val
            self._memo[self._capacity * index:self._capacity * (index + 1)] = tempStack
            self._stackCnt[index] += 1
            if self._stackCnt[index] >= self._capacity:
                ##push满了，移除这个index
                self._notFull.remove(index)
        else:##全满了或者刚开始
            # self._numOfStack += 1
            self._memo += [-1]* self._capacity
            self._memo[self._capacity * len(self._stackCnt.keys())] = val
            self._stackCnt[len(self._stackCnt.keys())] = 1
            if self._stackCnt[len(self._stackCnt.keys())-1] < self._capacity:
                self._notFull.add(len(self._stackCnt.keys())-1)
        print(self._stackCnt)


    def pop(self) -> int:
        index = len(self._stackCnt.keys()) - 1
        print("index:",index)
        while self._stackCnt[index] == 0 and index>0:
            print("cnt-:", self._stackCnt[index])
            index -= 1
        if self._stackCnt[index] == 0:
            return -1
        tempStack = self._memo[self._capacity * index:self._capacity * (index + 1)]
        res = tempStack[self._stackCnt[index]-1]
        tempStack[self._stackCnt[index]-1] = -1
        self._notFull.add(index)
        self._stackCnt[index] -= 1
        self._memo[self._capacity * index:self._capacity * (index + 1)] = tempStack
        return res


    def popAtStack(self, index: int) -> int:
        print(self._stackCnt)
        tempStack = self._memo[self._capacity*index:self._capacity*(index+1)]
        if len(tempStack) == 0:
            return -1
        # for i in range(len(tempStack)-1,-1,-1):
        if self._stackCnt[index] == 0:
            return -1
        else:

            res = tempStack[self._stackCnt[index]-1]
            tempStack[self._stackCnt[index] - 1 ] = -1
            self._stackCnt[index] -= 1
            self._notFull.add(index)
            self._memo[self._capacity * index:self._capacity * (index + 1)] = tempStack
            return res


["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]

dpl = DinnerPlates(2)
dpl.push(1)
dpl.push(2)
dpl.push(3)
dpl.push(4)
dpl.push(5)

dpl.popAtStack(0)
dpl.push(20)
dpl.push(21)

dpl.popAtStack(0)
dpl.popAtStack(2)

dpl.pop()
dpl.pop()
dpl.pop()
dpl.pop()
dpl.pop()












