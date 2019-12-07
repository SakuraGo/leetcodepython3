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
            self.stack.pop()   ##原来的理解有问题，一旦出现了比之前数更大的price，之前的小price的索引就没必要存在在stack中了。已经和结果没关系了

        if not self.stack:
            ans = self.length + 1
        else:
            ans = self.length - self.stack[-1]
        self.stock.append(price)
        self.stack.append(self.length)

        self.length += 1

        return ans

obj=StockSpanner()
obj.next(100)
obj.next(99)
obj.next(80)
obj.next(90)
obj.next(124)
obj.next(98)