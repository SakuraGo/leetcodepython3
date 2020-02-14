from  typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [-1 for i in range(n+1)]
        dp[0] = 0

        for idx in range(0,n+1):
            ran = ranges[idx]
            l = max(0,idx-ran)
            r = min(n,idx+ran)

            if dp[l] == -1:
                continue
            else:
                for pos in range(l,r+1):
                    print(pos)
                    if dp[pos]>=0:
                        dp[pos] = min(dp[pos],dp[l]+1)
                    else:
                        dp[pos] = dp[l]+1

        print(dp)
        return dp[n]

res = Solution().minTaps(n = 5, ranges = [3,4,1,1,0,0])
print(res)



