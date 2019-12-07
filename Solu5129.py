# 5129. 表现良好的最长时间段
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
# 请你返回「表现良好时间段」的最大长度。
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。

from typing import List
class Solution:
    # for i in range(0, len(dataLis) - mid):
    #     summm = preSum[i + mid] - preSum[i]
    #     if summm > 0:
    def isOK(self,dataLis:List[int],preSum:List[int], mid:int):
        minV = 99999
        for i in range(0, len(dataLis) - mid+1):
            ## 不是要以一个固定死的长度去 滑动窗口遍历 数组，
            # 而是要记下最小的那一个，如果 之后有节点减去该最小点大于0的话，
            # 就说明一定存在一个更长的长度可以满足要求，故返回True
            minV = min(minV,preSum[i])

            summm = preSum[i + mid] - minV
            if summm > 0:
                print("mid= %d :True" % mid)
                return True
        return False

    def longestWPI(self, hours: List[int]) -> int:
        dataLis = []

        for h in hours:
            if h>8:
                dataLis.append(1)
            else:
                dataLis.append(-1)

        print(dataLis)
        ##寻找最长的sum>1的一串数
        #preSum[i]  以第i个为结尾的dataLis之前的sum和
        preSum = [0]  ##需要有一个preSum0, 以方便求解 sum(x~y) =  preSum[y] - preSum[x-1]
        for num in dataLis:
            preSum.append(preSum[-1]+num)
        print(preSum)
        l = 0
        r = len(preSum)-1
        while (l<r):
            mid = int((l + r + 1) / 2)
            if self.isOK(dataLis,preSum,mid):
                l = mid
            else:
                r = mid-1
        return l

        # return maxLen

aaa = [9,6,9]
res = Solution().longestWPI(aaa)
print(res)




