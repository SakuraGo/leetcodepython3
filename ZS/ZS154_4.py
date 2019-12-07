# 5192. 查找集群内的「关键连接」

# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。
#
# 它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。
#
# 从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
#
# 「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
#
# 请你以任意顺序返回该集群内的所有 「关键连接」。
#
# 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。


from  typing import  List
class Solution:
    ##寻找桥的问题
    def __init__(self):
        self._visited = []
        self._ord = []
        self._low = []
        self._cnt = 0
        self._memoAdj = []
        self._res = []

    def dfs(self,node:int,parent):
        # child = 0
        print("node:",node,parent)
        self._visited[node] = 1
        self._ord[node] = self._cnt
        self._low[node] = self._cnt
        self._cnt+= 1
        for childNode in self._memoAdj[node]:
            if self._visited[childNode] == 1 and childNode!= parent: ##已访问
                self._low[node] = min(self._low[node],self._low[childNode])
            elif self._visited[childNode] == 0 : ##未访问
                self.dfs(childNode,node)
                self._low[node] = min(self._low[node],self._low[childNode])
                if self._low[childNode] > self._ord[node]:
                    self._res.append([node,childNode])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self._memoAdj = [[] for i in range(n)]
        self._visited = [0] * n
        self._ord = [0]*n
        self._low = [0]*n
        for conn in connections:
            node0,node1 = conn
            self._memoAdj[node0].append(node1)
            self._memoAdj[node1].append(node0)
        print(self._memoAdj[0])

        self.dfs(0,0)

        return self._res

res  = Solution().criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]])
print(res)