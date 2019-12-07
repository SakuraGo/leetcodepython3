# 5037. 平行课程  显示英文描述
# 题目难度 Hard
# 已知有 N 门课程，它们以 1 到 N 进行编号。
#
# 给你一份课程关系表 relations[i] = [X, Y]，用以表示课程 X 和课程 Y 之间的先修关系：课程 X 必须在课程 Y 之前修完。
#
# 假设在一个学期里，你可以学习任何数量的课程，但前提是你已经学习了将要学习的这些课程的所有先修课程。
#
# 请你返回学完全部课程所需的最少学期数。
#
# 如果没有办法做到学完全部这些课程的话，就返回 -1。

# 输入：N = 3, relations = [[1,3],[2,3]]
# 输出：2
# 解释：
# 在第一个学期学习课程 1 和 2，在第二个学期学习课程 3。
from typing import  List
class Solution:
    def __init__(self):
        self._data = [None]
        self._visited = None
        self._memo = None
        self._spasityData = None

    # def bfs(self,index:int):  ##O(N^2)超时
    #     print(index)
    #     self._visited[index] = 1
    #     for toIndex,j in enumerate(self._data[index]):
    #         if j > 0:
    #             if self._visited[toIndex]>0:
    #                 return False
    #             else:
    #                 return self.bfs(toIndex)
    #     return True

    def bfs(self, index: int):
        print(index)
        self._visited[index] = 1
        for toIndex in self._spasityData[index]:
            if self._visited[toIndex]>0:
                return False
            else:
                return self.bfs(toIndex)
        return True

    def bianliGraph(self,index:int):
        self._visited[index] = 1
        if self._memo[index] > 0:
            return self._memo[index]
        maxx = 1
        for toIndex,j in enumerate(self._data[index]):
            if j > 0:
                maxx = max(maxx,self.bianliGraph(toIndex)+1)

        self._memo[index] = maxx
        return self._memo[index]



    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        self._data = [None] * N
        self._spasityData = [None] * N
        for i in range(N):
            self._data[i] = [0] * N
            # self._spasityData = [0] * N
            lis = list()
            self._spasityData[i] = lis

        for lis in relations:
            i , j = lis
            self._data[i-1][j-1] = 1
            self._spasityData[i-1].append(j-1)



        self._visited = [-1] * N

        for i in range(N):
            self._visited = [-1] * N
            if self._visited[i]<0:
                flag = self.bfs(i)
                if flag is False:
                    return -1
        print("==========")
        self._visited = [-1] * N ## 重置
        self._memo = [-1] * N
        maxx = -111
        res = 0
        for course0,course1 in relations:

            course = course0 - 1
            if self._visited[course] > 0:
                continue
            res = max(res,self.bianliGraph(course))

        return res




res = Solution().minimumSemesters(3,[[1,3],[2,3]])
print(res)