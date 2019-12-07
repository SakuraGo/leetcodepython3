# 5132. 颜色交替的最短路径
# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。
#
# red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。
#
# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的最短路径的长度，且路径上红色边和蓝色边交替出现。如果不存在这样的路径，那么 answer[x] = -1。

# 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]

from typing import List
import queue

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # red_data = [None] * n
        # blue_data = [None] * n
        # for i in range(n):
        #     lis = [0] * n
        #     red_data[i] = lis
        # for i in range(n):
        #     lis = [0] * n
        #     blue_data[i] = lis
        #
        # visited = [None] * n #记录是否被访问过。。 [n][0]下一个边是红色 [n][1] 下一个边是蓝色
        # for i in range(n):
        #     lis = [0] * 2
        #     visited[i] = lis
        #
        # for data in red_edges:
        #     i ,j = data
        #     red_data[i,j] = 1
        #
        # for data in blue_edges:
        #     i,j = data
        #     blue_data[i,j] = 1
        #
        # ord = [None] * n    ##[n][0]下一个边是红色的ord
        # for i in range(n):
        #     lis = [-1] * 2
        #     ord[i] = lis
        #
        # q = queue.Queue()
        # q.put(0)
        # visited[0][0] = 1
        # ord[0][0] = 0
        # rbFlag = True
        # while  q.empty() == False:
        #     print("非空")
        #     x = q.get()
        #     flag = 0
        #     if rbFlag is True:
        #         lis = red_data[x]
        #         flag = 0  # 下一个红色
        #     else:
        #         lis = blue_data[x]
        #         flag = 1 # 下一个蓝色
        #     for index,num in enumerate(lis):
        #         if num == 1:
        #             if visited[index][flag] != 1:
        #                 q.put(index)
        #                 ord[index][flag] =
        ##写到这里感觉有点问题，需要构建一个类，可以存放index与是否下一个是红色的类
        # 。。。











        return [1]


arr = [1,2]
i ,j = arr
print(j)

q = queue.Queue()
q.put(2)
print(q.empty())
q.put(None)
ttt = False
ttt = not ttt
print(  ttt)