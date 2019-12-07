# 5098. 树的直径  显示英文描述  我的提交返回竞赛
# 用户通过次数 18
# 用户尝试次数 20
# 通过次数 18
# 提交次数 20
# 题目难度 Medium
# 我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。
#
# 树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。
#
# 给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。

from typing import List
class Solution:
    def __init__(self):
        self._graph = {}
        self._visited = []
        self._res = 0 ##纪录最大
    ##返回该节点的深度。。
    def dfs(self,node,fromN):
        self._visited[node] = 1
        children = self._graph[node]
        if self._visited[children[0]] == 1 and self._visited[children[-1]] == 1:

            return 0
        deps = [0 for i in range(len(children))]

        for idx,nod in enumerate(children):
            if self._visited[nod] == 1:
                continue
            else:
                deps[idx] = self.dfs(nod,node)
        deps = sorted(deps,reverse=True)
        if len(deps)>= 2:
            self._res = max(self._res,deps[0]+deps[1]+2)

        return deps[0]+1


    def treeDiameter(self, edges: List[List[int]]) -> int:
        for pair in edges:
            p0,p1 = pair
            if p0 in self._graph.keys():
                self._graph[p0].append(p1)
            else:
                self._graph[p0] = [p1]
            if p1 in self._graph.keys():
                self._graph[p1].append(p0)
            else:
                self._graph[p1] = [p0]

            self._visited = [-1 for i in range(len(self._graph))]

        # for nod in self._graph.keys():
        #     print(nod)
        #     self._res = max(self._res,self.dfs(nod,nod))
        #     self._visited =  [-1 for i in range(len(self._graph))]
        dep = self.dfs(0,0)
        self._res = max(self._res,dep)

        return self._res


res = Solution().treeDiameter([[0,1],[0,2]])
print(res)
