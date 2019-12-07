from  typing import List
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return sticks[0]

        sum = 0
        heapq.heapify(sticks)
        while len(sticks)>1:
            #
            num0 = heapq.heappop(sticks)
            num1 = heapq.heappop(sticks)
            sum += (num0+num1)
            heapq.heappush(sticks,(num0+num1))
            heapq._siftup(sticks,len(sticks)-1)
            # print(sticks)

        return sum

#
# lis = [5,1,2,3,3,3,5]
# heapq.heapify(lis)

# print(lis)

res =  Solution().connectSticks([8,1,3,5])

print(res)
# print(1397754 - 1363767)