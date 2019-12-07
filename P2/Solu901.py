# 901. 股票价格跨度  显示英文描述
# 用户通过次数 68
# 用户尝试次数 126
# 通过次数 68
# 提交次数 420
# 题目难度 Medium
# 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
#
# 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
#
# 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。


class MemoModel:
    def __init__(self,num,index):
        self._num = num
        self._index = index

class StockSpanner:

    def __init__(self):
        self._data = []
        self._memoLis = []

    def next(self, price: int) -> int:
        self._data.append(price)
        self._memoLis.append(MemoModel(price, len(self._data)-1))
        self._memoLis.sort(key=lambda x:x.num,reverse=True) # 大到小.





        return  1
