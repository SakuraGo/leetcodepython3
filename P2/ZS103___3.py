from typing import  List
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        aaa = set(A)
        a = min(aaa)
        b = max(aaa)
        sortedA = sorted(aaa)
        print(sortedA)
        res = b - a

        for idx,num  in enumerate(sortedA):
            print("num:",num)
            if idx == len(sortedA)-1:
                return res
            if num+2*K<=sortedA[-1]:
                sortedA[idx] = num + 2* K
                a = min(sortedA[0],sortedA[idx+1])
                res = min(res,sortedA[-1]-a)
                print("sortedA:", sortedA)
                continue
            else:
                b = max(b,num+ 2*K)
                sortedA[idx] = num + 2 * K
                a = min(sortedA[0],sortedA[idx + 1])
                newRes  = b - a
                if newRes>=res:
                    return res
                else:

                    res = min(res,newRes)
                    print("sortedA:",sortedA)

res = Solution().smallestRangeII([506,4763,8681,4243,4040,8587,9235,442,1865,2820],5899)
print(res)