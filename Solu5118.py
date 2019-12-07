# 5118. 航班预订统计
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
# 我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
#
# 请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]

from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for lis in bookings:
            for i in range(lis[0]-1,lis[1]):
                res[i] += lis[2]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+2)
        for starti,endi,vals in bookings:
            res[starti-1]+= vals
            res[endi+1] -=vals

        for i in range(1,len(res)):
            res[i] += res[i-1]

        return res[1:-1]





'''
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        s = [0] * (n + 2)               
        for i, j, k in bookings:         ###累计增量的方法。。
            s[i] += k                       ##O(n)复杂度
            s[j + 1] -= k
            
        for i in xrange(1, n + 1):
            s[i] += s[i - 1]                ##累计之前的结果，如果要消除这个增加量，就在 j处减去 k,使得s[j+1] 消去 k，这样之后的累计过程就不会再增加k了。。
            
        return s[1: n + 1]
'''


res = [12]*5
res1 = [23]*5
print(res+res1)