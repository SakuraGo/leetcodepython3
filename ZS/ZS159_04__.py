
from typing import  List
class Solution:

    def __init__(self):
        self._res = 0
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        all_data = []
        for idx in range(len(endTime)):
            all_data.append((startTime[idx],endTime[idx],profit[idx]))

        all_data = sorted(all_data,key=lambda x:x[1])
        # print(all_data)
        # startTime = [all_data[i][0] for i in range(len(all_data))]
        # endTime = [all_data[i][1] for i in range(len(all_data))]
        # profit = [all_data[i][2] for i in range(len(all_data))]


        # dp = [[0 for j in range(all_data[-1][1]+1)] for i in range(len(profit))]  ##n*m可行但超时了 ..

        dp = [0 for j in range(all_data[-1][1]+1)] ##单行dp

        ##初始化
        for j in range(len(dp)):
            if j < all_data[0][1]:
                continue
            else:
                dp[j] = all_data[0][2]  ##初始化.

        self._res = max(self._res,profit[0])

        ##使用一个标记点记录上一个的end的位置。。end是一个关键节点。。
        jstart = all_data[0][0]

        ##单行dp
        for i in range(1,len(all_data)):
            s,e,p = all_data[i]
            for j in range(jstart,e+1):
                dp[j] = max(dp[j],dp[j-1])
                if j == e:
                    dp[j] = max(dp[j],dp[s]+p)
                    self._res = max(self._res,dp[j])
            jstart = e
        print(dp)
        return self._res



        ##
        # for i in range(1,len(dp)):
        #     for j in range(jstart,endTime[i]+1):  ##从时间复杂度方向考虑需要有这么一手..
        #         if j < endTime[i]: ##只能不加入这个profit
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             # j == all_data[i][1]:
        #             dp[i][j] = max(dp[i-1][j],dp[i][all_data[i][0]]+all_data[i][2])  ##之前的信息置零了。。
        #             self._res = max(self._res, dp[i][j])
        #         # else:
        #         #     dp[i][j] = dp[i][j-1]
        #     jstart = endTime[i]


        return self._res

res = Solution().jobScheduling([6,24,45,27,13,43,47,36,14,11,11,12],[31,27,48,46,44,46,50,49,24,42,13,27],[14,4,16,12,20,3,18,6,9,1,2,8])
print(res)

