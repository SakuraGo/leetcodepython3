# 5072. 最多可以买到的苹果数量  显示英文描述  我的提交返回竞赛
#
# 楼下水果店正在促销，你打算买些苹果，arr[i] 表示第 i 个苹果的单位重量。
#
# 你有一个购物袋，最多可以装 5000 单位重量的东西，算一算，最多可以往购物袋里装入多少苹果。


from typing import List
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        summ = sum(arr)
        maxxweight = 5000
        if summ< maxxweight:
            return len(arr)
        else:
            sa = sorted(arr)
            qSum = 0
            resCnt = 0
            for weight in  sa:
                qSum += weight
                if qSum < maxxweight:
                    resCnt+=1

            return resCnt