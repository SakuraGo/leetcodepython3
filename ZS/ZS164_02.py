# 5272. 统计参与通信的服务器  显示英文描述  我的提交返回竞赛
# 用户通过次数 348
# 用户尝试次数 398
# 通过次数 349
# 提交次数 471
# 题目难度 Medium
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
#
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
#
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

from  typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        fugaigrid = [[0 for jj in range(len(grid[0]))] for ii in range(len(grid))]
        # rowMemo = [0 for ii in range(len(grid))]
        # colMemo = [0 for jj in range(len(grid[0]))]
        yiliuList = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                else:
                    # if rowMemo[i] == 1 or colMemo[j] == 1:
                    if fugaigrid[i][j] == 1:
                        res += 1
                    else:
                        yiliuList.append([i,j])

                    for iii in range(len(fugaigrid)):
                        fugaigrid[iii][j] = 1
                    for jjj in range(len(fugaigrid[0])):
                        fugaigrid[i][jjj] = 1
                    fugaigrid[i][j] = 0
        for point in yiliuList:
            r,c = point
            if fugaigrid[r][c] == 1:
                res += 1

        return res




