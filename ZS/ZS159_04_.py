'''
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(profit)
        time = []
        for i in range(n):
            time.append([startTime[i], endTime[i], profit[i]])
        time.sort(key=lambda x: x[1])
        max_ = time[-1][1]
        dp = [0] * (max_ + 1)
        last = 0
        for s, e, p in time:
            for j in range(last + 1, e + 1):
                dp[j] = max(dp[j], dp[j - 1])
            dp[e] = max(dp[e], dp[s] + p)
            last = e
        return dp[-1]
'''

'''
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
'''