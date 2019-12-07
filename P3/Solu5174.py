# 5174. 健身计划评估  显示英文描述
#
# 你的好友是一位健身爱好者。前段日子，他给自己制定了一份健身计划。现在想请你帮他评估一下这份计划是否合理。
#
# 他会有一份计划消耗的卡路里表，其中 calories[i] 给出了你的这位好友在第 i 天需要消耗的卡路里总量。
#
# 一份计划的周期通常是 k 天，你需要计算他在这 k 天内消耗的总卡路里 T：
#
# 如果 T < lower，那么这份计划相对糟糕，并失去 1 分；
# 如果 T > upper，那么这份计划相对优秀，并获得 1 分；
# 否则，这份计划普普通通，分值不做变动。
# 请返回统计完所有 calories.length 天后得到的总分作为评估结果。
#
# 注意：总分可能是负数。


from typing import List
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        c0 = 0
        index = 0
        for i in range(0,k):
            c0 += calories[i]
            index += 1

        cur = c0
        res = 0

        while index < len(calories):
            ##
            if cur < lower :
                res -= 1

            elif cur>upper:
                res += 1
            else:
                res += 0

            cur += calories[index]
            cur -= calories[index-k]
            index += 1

        if cur < lower:
            res -= 1

        elif cur > upper:
            res += 1
        else:
            res += 0

        return res