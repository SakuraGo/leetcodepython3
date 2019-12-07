# 576. 出界的路径数

# 给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，
# 你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。
# 但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        mod = 1000000007
        if (N<1):
            return 0
        ##这样先创建再填充，各个行列之间才会独立
        memo = [None] * N
        for k in range(N):
            memo0 = [None] * m
            for q in range(m):
                memo0[q] = [0] * n
            memo[k] = memo0

        for k in range(m):
            memo[0][k][0] +=1
            memo[0][k][n-1] +=1

        for k in range(n):
            memo[0][0][k] +=1
            memo[0][m-1][k] +=1

        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        deleLayer = [[0] * n]*m
        def isValidPos(iPos,jPos):
            return (iPos>=0 ) & (iPos<m) & (jPos >=0) & (jPos<n)
        for c in range(1,N):
            for p in range(m):
                for q in range(n):
                    dataLayer = memo[c-1]

                    if c>=2 :
                        deleLayer = memo[c-2]
                    sum = memo[c-1][p][q]
                    for r in dir:
                        if isValidPos(p+r[0],q+r[1]):
                            sum = sum+dataLayer[p+r[0]][q+r[1]] - deleLayer[p+r[0]][q+r[1]]

                    memo[c][p][q] = sum

        return  memo[N-1][i][j]%mod

res = Solution().findPaths(1,2,6,0,0)
print(res)