#
# Problem 4
# 这个是典型的轮廓线动态规划题目。每次放置考虑从上到下，从左至右放置。按照这种规律放的话，每次放置，只需要记录从上一行的该格子到该格子前一个的状态。使用状态压缩转为 2 进制即可很方便使用 dp 进行转移。
#
# But... 如果说记录全盘的状态，则状态数会高达 O(2mn)O(2^{mn})O(2mn)，在这道题的范围下，状态数堪比棋盘上的麦粒那么多。显然，需要一定技巧来减少需要记录的状态量。
from typing import List
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        brk = set()
        for b in broken:
            brk.add((b[0],b[1]))
        dp = [-1]*(1<<(m+1))
        block = (1<<(m+1))-1
        dp[(1<<(m+1))-1] = 0
        for i in range(n):
            next_dp = [-1]*(1<<(m+1))
            for state in range(1<<(m+1)):
                if block & state != block or dp[state] == -1:
                    continue
                next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state])
            block = (block>>1) | (1<<m)
            print("block:",block)
            dp = next_dp

            for j in range(m):
                next_dp = [-1]*(1<<(m+1))
                next_block = block>>1
                print("nB:",next_block)
                for state in range(1<<(m+1)):
                    if block & state != block or dp[state] == -1:
                        continue
                    if (i,j) in brk:
                        next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state])
                        next_block = next_block | (1<<m)
                    else:
                        next_dp[state>>1] = max(next_dp[state>>1], dp[state])
                        if state & 1 == 0:
                            next_dp[(state>>1)|(1<<m)] = max(next_dp[(state>>1)|(1<<m)], dp[state]+1)
                        if state & (1<<m) == 0:
                            next_dp[(state>>1)|(1<<m)|(1<<(m-1))] = max(next_dp[(state>>1)|(1<<m)|(1<<(m-1))], dp[state]+1)
                dp = next_dp
                block = next_block

        print()
        return max(dp)

res = Solution().domino(3,3,[])
print(res)
print()
print(1&2)
print(1|2)