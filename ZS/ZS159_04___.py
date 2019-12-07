from typing import  List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        disc, cur = {}, 0
        all_times = sorted(list(set(startTime + endTime)))
        for i in all_times:
            disc[i] = cur
            cur += 1
        pp = sorted(list(zip([disc[i] for i in startTime], [disc[i] for i in endTime], profit)), key=lambda x: x[1])
        print(pp)
        cur_index, dp = 0, [0] * (cur)
        for i, num in enumerate(dp):
            print(i,num)
            while cur_index < len(pp) and i == pp[cur_index][1]:
                current_p = pp[cur_index]
                dp[i] = max(dp[i], dp[current_p[0]] + current_p[2])
                cur_index += 1
            if i > 0:
                dp[i] = max(dp[i - 1], dp[i])
        return dp[len(dp) - 1]

res = Solution().jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])
print(res)