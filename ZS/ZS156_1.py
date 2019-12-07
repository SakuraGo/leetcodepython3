# 5205. 独一无二的出现次数  显示英文描述
# 用户通过次数 60
# 用户尝试次数 75
# 通过次数 60
# 提交次数 76
# 题目难度 Easy
# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

from typing import  List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntDic = {}
        for num in arr:
            if num in cntDic.keys():
                cntDic[num] += 1
            else:
                cntDic[num] = 1

        memoSet = set()
        for k,v in cntDic.items():
            if v in memoSet:
                return False
            else:
                memoSet.add(v)

        return True