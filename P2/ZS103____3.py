from typing import  List
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        sa = sorted(A)
        res = sa[-1] - sa[0]

        preNum = -99
        for idx,num in enumerate(sa):
            if num == preNum or idx == len(sa)-1:
                continue
            bmax = max(num+K,sa[-1]-K)
            bmin = min(sa[0]+K,sa[idx+1]-K)
            res = min(res,bmax-bmin)
        return res


res = Solution().smallestRangeII([506,4763,8681,4243,4040,8587,9235,442,1865,2820],5899)
print(res)