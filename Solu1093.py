# 1093. 大样本统计  显示英文描述
#
# 题目难度 Medium
# 我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 意味着采样的整数为 k。
#
# 我们以 浮点数 数组的形式，分别返回样本的最小值、最大值、平均值、中位数和众数。其中，众数是保证唯一的。
#
# 我们先来回顾一下中位数的知识：
#
# 如果样本中的元素有序，并且元素数量为奇数时，中位数为最中间的那个元素；
# 如果样本中的元素有序，并且元素数量为偶数时，中位数为中间的两个元素的平均值。
from typing import List


class Solution:
    def __init__(self):
        self._min = -1
        self._max = 0
        self._maxCnt = 0
        self._zhongShu = 0
        self._flagNum0 = 0
        self._flagNum1 = 0
        self._average = 0
    def sampleStats(self, count: List[int]) -> List[float]:
        summm = 0
        numSCount = sum(count) ##数的个数
        med0 = 0
        med1 = 1
        if numSCount%2 == 0:
            med0 = numSCount/2 -1
            med1 = numSCount/2
        else:
            med0 = int(numSCount/2)
            med1 = int(numSCount/2)
        curCnt = 0
        for nummm in range(256):
            cnt = count[nummm]
            if (cnt>0) & (self._min < 0):
                self._min = nummm

            if (cnt>0):
                self._max = nummm
            if (cnt > self._maxCnt):
                self._maxCnt = cnt
                self._zhongShu = nummm

            summm += cnt * nummm
            if (curCnt<=med0) & (curCnt+cnt > med0):
                self._flagNum0 = nummm
            if (curCnt<=med1) & (curCnt+cnt > med1):
                self._flagNum1 = nummm
            curCnt += cnt

        self._average = summm/numSCount

        zws = (self._flagNum0 + self._flagNum1)/2
        return [self._min/1.0,self._max/1.0,self._average/1.0,zws/1.0,self._zhongShu/1.0]

asd = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# res = Solution().sampleStats(asd)
# print(res)
res = Solution().sampleStats(asd)
