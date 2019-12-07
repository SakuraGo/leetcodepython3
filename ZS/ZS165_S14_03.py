# 5114. 删除树节点  显示英文描述  我的提交返回竞赛
# 用户通过次数 33
# 用户尝试次数 37
# 通过次数 33
# 提交次数 39
# 题目难度 Medium
# 给你一棵以节点 0 为根节点的树，定义如下：
#
# 节点的总数为 nodes 个；
# 第 i 个节点的值为 value[i] ；
# 第 i 个节点的父节点是 parent[i] 。
# 请你删除节点值之和为 0 的每一棵子树。
#
# 在完成所有删除之后，返回树中剩余节点的数目。
from  typing import List
class Solution:
    def __init__(self):
        self._cnt = 0
        self._val = []
        self._children = {}

    def dfsTree(self,idx):
        if idx not in self._children:
            if self._val[idx] == 0:
                self._cnt += 1
                return 0,0

            return self._val[idx],1  ##返回: 数值 和 节点个数
        summ = 0
        summ += self._val[idx]
        cntt = 1
        for childIdx in self._children[idx]:
            s,cnt = self.dfsTree(childIdx)
            summ += s
            cntt += cnt

        if summ == 0:
            self._cnt += cntt
            return 0,0
        else:
            return summ,cntt


    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        self._val = value
        maxx = max(parent)
        for fat in range(0,maxx+1):
            self._children[fat] = []

        for  idx,par in enumerate(parent):
            if par == -1 :
                continue
            # if idx>maxx:
            #     break
            self._children[par] .append(idx)

        self.dfsTree(0)

        return nodes - self._cnt

asd  = Solution().deleteTreeNodes(7,[-1,0,0,1,2,2,2],[1,-2,4,0,-2,-1,-1])
print(asd)