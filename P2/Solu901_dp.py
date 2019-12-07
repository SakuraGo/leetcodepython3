class StockSpanner:

    def __init__(self):
        self._data = []
        self._memoDays = []
        self._len = 0


    def next(self, price: int) -> int:
        res = 1
        i = self._len-1

        while  i >=0 and self._data[i] <= price:
            res += self._memoDays[i]
            i -= self._memoDays[i]

        self._data.append(price)
        self._memoDays.append(res)
        self._len += 1

        return res

obj = StockSpanner()
obj.next(100)
obj.next(38)

'''
记录每个节点的price大小，从右向左看，res和与之最近的比他更大的那个数的索引相关
做减法就可得连续小于price的天数
使用单调栈 作为辅助

class StockSpanner:

    def __init__(self):
        self.stock = []
        self.stack = []
        self.length = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 0
        while self.stack and self.stock[self.stack[-1]] <= price:
            self.stack.pop()
        
        if not self.stack:
            ans = self.length + 1
        else:
            ans = self.length - self.stack[-1]
        self.stock.append(price)
        self.stack.append(self.length)
        
        self.length += 1
        
        return ans
'''

