# 199. 二叉树的右视图
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeFlag:
    def __init__(self,x,nodeee):
        self.floor = x
        self.node = nodeee

import queue
from typing import  List

class Solution:
    def __init__(self):
        self._q = queue.Queue()

        self._res = []

    def handleRot(self):
        preX = -1
        while self._q.qsize()>0:
            cur = self._q.get()
            floor = cur.floor
            node = cur.nodeee
            if floor > preX:
                self._res.append(node.val)
                preX = floor
            if node.right is not None:
                self._q.put(TreeFlag(floor+1,node.right))
            if node.left is not None:
                self._q.put(TreeFlag(floor+1,node.left))


    def rightSideView(self, root: TreeNode) -> List[int]:


        if root is None :
            return self._res

        rot = TreeFlag(0,root)
        self._q.put(rot)
        self.handleRot()
        return self._res



print(99//5)

