# 5282. 转化为全零矩阵的最少反转次数  显示英文描述  我的提交返回竞赛
# # 用户通过次数 0
# # 用户尝试次数 1
# # 通过次数 0
# # 提交次数 1
# # 题目难度 Hard
# # 给你一个 m x n 的二进制矩阵 mat。
# #
# # 每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。（注：相邻的两个单元格共享同一条边。）
# #
# # 请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。
# #
# # 二进制矩阵的每一个格子要么是 0 要么是 1 。
# #
# # 全零矩阵是所有格子都为 0 的矩阵。

from  typing import List
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        weishu = m*n
        maxx = (1<< (weishu)) -1
        target = 0
        memoset = set()

        def mat2num(mat):
            sum = 0
            for row,nums in enumerate(mat):
                for col,num in enumerate(nums):
                    pianyi = row*n + col
                    sum += num<<pianyi
            return sum

        memoset.add(mat2num(mat))

        def num2mat(nummm,m,n):
            mattt = [[0]*n for _ in range(m)]
            for row, nums in enumerate(mattt):
                for col, num in enumerate(nums):
                    # for i in xrange(len(bin_num)):
                    #     if (1 << i) & int_num:
                    #         print
                    #         " the number '1' position is " + str(i)
                    # mattt[row][col] = ((1<<(row*n+col)) & nummm)
                    mattt[row][col] = ((nummm >> (row*n+col))&1)
            print(mattt,nummm)
            return mattt

        if mat2num(mat) == 0:
            return 0
        statusLis = [(mat2num(mat),0)]
        while len(statusLis)>0:
            status,step = statusLis.pop(0)
            print(status,step)
            curMat = num2mat(status,m,n)
            for i in range(m):
                for j in range(n):
                    curCopy = num2mat(status,m,n)
                    curCopy[i][j] = 1-curCopy[i][j]
                    if i>0:
                        curCopy[i-1][j] = 1 - curCopy[i-1][j]
                    if j>0:
                        curCopy[i][j-1] = 1- curCopy[i][j-1]
                    if i<m-1:
                        curCopy[i+1][j] = 1 - curCopy[i+1][j]
                    if j<n-1:
                        curCopy[i][j+1] = 1 - curCopy[i][j+1]
                    newStatus = mat2num(curCopy)
                    if newStatus not in memoset:
                        if newStatus == 0:
                            return step+1
                        statusLis.append((newStatus,step+1))
                        memoset.add(newStatus)

        # return 123
        print(memoset)
        return -1


res = Solution().minFlips([[0]])
print(1<<9)
print(res)