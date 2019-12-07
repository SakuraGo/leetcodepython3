from typing import  List
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        maxxx = max(A)
        minnn = min(A)
        newMin = minnn + K
        newA = (sorted(A))
        print(newA)
        amin = newMin
        amax = 0
        for idx ,num in enumerate(newA): ##第一次遍历，刷新新数组上界
            if num < newMin:

                amax = max(amax,num + K)
                continue
            if num >= newMin + K:
                # newA[idx] = num - K
                amax = max(amax,num-K)
                continue
        print(amax,amin)

        for num in newA[::-1]:
            if num>=newMin and num < newMin + K:
                print("num:",num)

                upchaju = amax - num - K
                downchaju = num-K - amin
                if upchaju >= 0 or downchaju>=0:
                    continue
                upX = abs(amax- num-K)
                downX = abs(num-K - amin)
                if upX<= downX:
                    amax = num+K
                else:
                    amin = num-K

        return amax - amin


res = Solution().smallestRangeII([7,8,8,5,2],4)
print(res)

