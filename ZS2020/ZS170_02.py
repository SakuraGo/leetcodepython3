# 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8]
# 解释：
# 数组中元素的二进制表示形式是：
# 1 = 0001
# 3 = 0011
# 4 = 0100
# 8 = 1000
# 查询的 XOR 值为：
# [0,1] = 1 xor 3 = 2
# [1,2] = 3 xor 4 = 7
# [0,3] = 1 xor 3 xor 4 xor 8 = 14
# [3,3] = 8

##异或前缀和思路
## 1....r  = A
## 1....l-1 = B
## 那么 l-r = A^B

from  typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # print(3^2)
        res = []
        memo = {}


        for pair in queries:
            l,r = pair
            idx = l
            xx = 0
            while idx<=r:
                if idx in memo and r>= memo[idx][1]:
                    num ,rr = memo[idx]
                    xx = xx^num
                    idx = rr+1
                else:

                    xx = xx^ arr[idx]
                    idx+= 1

            res .append(xx)
            if l not in memo:
                memo[l] = [xx,r]
            else:
                if r > memo[l][1]:
                    memo[l] = [xx,r]
        return res







res = Solution().xorQueries([2,8,13,6],[[2,3],[0,3],[0,1],[3,3],[3,3]])
print(res)