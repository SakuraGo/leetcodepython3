
from typing import  List
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left=0
        K+=1
        right = int(sum(sweetness)/K)
        while (left<=right):
            mid = int((left+right)/2)
            temp=0
            flag = 0
            re = False
            for x in sweetness:
                temp+=x
                if temp>=mid:
                    flag+=1
                    temp = 0
                if flag==K:
                    re = True
                    break
            if re:
                left = mid+1
                ans = mid
            else:
                right = mid-1
        return ans

res = Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], K = 5)
print(res)