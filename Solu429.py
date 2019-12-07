# 429. N叉树的层序遍历
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class qNod:
    def __init__(self,node,layer = 0):
        self._node = node
        self._layer = layer

import queue
from typing import  List
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []

        res = []
        qq = queue.Queue()

        qq.put(qNod(root,layer=0))
        while qq.qsize()>0:
            nod = qq.get()
            if len(res)<=nod._layer:
                newLis = [nod._node.val]
                res.append(newLis)
            else:
                res[nod._layer].append(nod._node.val)

            for chi in nod._node.children:
                newNod = qNod(chi,nod._layer+1)
                qq.put(newNod)

        return res



qqq = queue.Queue()
qqq.put(1)
qqq.put(33)
print(qqq.get())
print("qq")
print(qqq.qsize())

'''
## 字典记层
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        
        d={}
        def f(r,i=0):
            if i not in d:
                d[i]=[r.val]
            else:
                d[i]+=[r.val]
            for j in r.children:
                f(j,i+1)
        f(root)

        return list(d.values())
'''