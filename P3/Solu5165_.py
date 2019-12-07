from heapq import *
import heapq

##其实和我的想法很接近了，但是他熟练利用了 heapq
class DinnerPlates(object):

    def __init__(self, capacity):

        self.c = capacity  ## stack容量
        self.stack = []  ## 存储具体数据
        self.n = []  ##存那个stack 有空缺

    def push(self, val):

        if self.n:
            index = heapq.heappop(self.n)
            if index >= len(self.stack):
                self.stack.append([])
                index = len(self.stack) - 1
            self.stack[index].append(val)
            if len(self.stack[index]) < self.c:
                heapq.heappush(self.n, index)
        else:
            self.stack.append([])
            self.stack[-1].append(val)
            self.n.append(len(self.stack) - 1)

        print(self.n)

    def pop(self):
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if self.stack:
            if len(self.stack[-1]) == self.c:
                heapq.heappush(self.n, len(self.stack) - 1)
            return self.stack[-1].pop()
        else:
            return -1

    def popAtStack(self, index):
        if index < len(self.stack):
            s = self.stack[index]
            if s:
                if len(s) == self.c:
                    heapq.heappush(self.n, index)
                return s.pop()
            else:
                return -1
        else:
            return -1

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
