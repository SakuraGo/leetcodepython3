# 576. 出界的路径数

# 给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，
# 你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。
# 但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        ##这样先创建再填充，各个行列之间才会独立
        memo = [None] * 3
        for k in range(3):
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

        cnt = 1
        dataLayer = memo[0]
        newLayer = dataLayer
        deleLayer = None
        dir = [[0,1],[1,0],[-1,0],[0,-1]]

        def isValidPos(iPos,jPos):
            return (iPos>=0 ) & (iPos<m) & (jPos >=0) & (jPos<n)
        while (cnt<N):

            if (cnt<2):
                dataLayer = memo[0]
                newLayer = memo[1]
                deleLayer = memo[2] ##全是0，减不减无所谓
            else:
                newLayer = memo[2]
                dataLayer = memo[1]
                deleLayer = memo[0]

            for p in range(m):
                for q in range(n):
                    sum = dataLayer[p][q]
                    for r in dir:
                        if isValidPos(p+r[0],q+r[1]):
                            ###DP递进关系
                            ##  第N层每个[i,j]中存的是该点经过N步可以出界的路径个数
                            ##  因此DP关系就是，如果要在多加一步，那么附近所有格子正好经过N 步可以走出的路径数 + 本身存有的路径数，就是下一层(N+1)要求的数
                            ## 注意从附近的点中要提取的是 正好走了N步出界的个数 ，因为 走了其他步出界的路径数其实已经被存在 layerN[i,j]中。
                            ## 因此处理方法为 减去下下层的路径数
                            sum = sum+dataLayer[p+r[0]][q+r[1]] - deleLayer[p+r[0]][q+r[1]]   #

                    newLayer[p][q] = sum

            memo[0] = dataLayer
            memo[1] = newLayer
            # dataLayer = newLayer
            cnt += 1
        return  newLayer[i][j]

res = Solution().findPaths(1,2,50,0,0)
print(res)