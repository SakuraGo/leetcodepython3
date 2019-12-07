# # 1020. 飞地的数量
# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
#
# 移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
#
# 返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
# 输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
from  typing import List
class Solution:
    def __init__(self):
        self._visited = []
        self._aa = 0
        self._bb = 0






    def numEnclaves(self, A: List[List[int]]) -> int:
        aa = len(A)
        self._aa = aa
        bb = len(A[0])
        self._bb = bb
        # self._visited = [None] * aa

        def isValid(self, i: int, j: int):
            return i >= 0 and i < self._aa and j >= 0 and j < self._bb

        def dfs(self, i: int, j: int):
            if self.isValid(i, j) is False:
                return

            if A[i][j] == 0:
                return

            # self._visited[i][j] = 1
            A[i][j] = 0

            self.dfs(i+1,j)
            self.dfs(i-1,j)
            self.dfs(i,j+1)
            self.dfs(i,j-1)

        # for i in range(aa):
        #     lis = [0] * bb
        #     self._visited[i] = lis

        for i in range(self._aa):
            for j in [0,self._bb-1]:
                dfs(self,i,j)

        for j in range(self._bb):
            for i in [0,self._aa-1]:
                dfs(self,i,j)

        res = 0

        for i in range(self._aa):
            for j in range(self._bb):
                if A[i][j] == 1:
                    res += 1

        return res


# TypeError: dfs() missing 1 required positional argument: 'j'
# Line 43 in numEnclaves (Solution.py)
# Line 78 in _driver (Solution.py)
# Line 91 in <module> (Solution.py)

for j in [0,99]:
    print(j)


