# 5141. 最大的以 1 为边界的正方形
# 给你一个由若干
# 0
# 和
# 1
# 组成的二维网格
# grid，请你找出边界全部由
# 1
# 组成的最大
# 正方形
# 子网格，并返回该子网格中的元素数量。如果不存在，则返回
# 0。
#
# 示例
# 1：
#
# 输入：grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 输出：9
from typing import  List
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        maxx = -1

        bb = len(grid[0])
        aa = len(grid)
        print("aa:",aa)
        print("bb:",bb)
        minab = min(aa,bb)

        for i in range(aa):
            for j in range(bb):
                startP = grid[i][j]
                if startP == 0:
                    continue

                bianchang = 1
                while(bianchang+i-1 < aa and bianchang + j -1 < bb):
                    print("i:%s,j:%s"%(i,j))
                    print("bianchang:",bianchang)
                    if grid[i][j+bianchang-1] == 0 or grid[i+bianchang-1][j] == 0:
                        break
                    gridFlag = True
                    for x in range(bianchang):
                        if grid[i+bianchang-1][j+x] == 0 or grid[i+x][j+bianchang-1] == 0:
                            gridFlag = False
                            break
                    if gridFlag is True:
                        maxx = max(maxx,bianchang)
                        print("maxx:",maxx)

                    bianchang+=1

        if maxx<0:
            return 0
        else:
            return maxx*maxx


res = Solution().largest1BorderedSquare([[0,0,0,1]])
print(res)






        
