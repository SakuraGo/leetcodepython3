
# 501. 二叉搜索树中的众数
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def __init__(self):
        self._res = {}

    def bianli(self,node:TreeNode):
        if node is None:
            return

        self.bianli(node.left)

        if node.val in self._res:
            self._res[node.val] += 1
        else:
            self._res[node.val] = 1

        self.bianli(node.right)



    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return self._res

        self.bianli(root)

        lis =list(self._res.items())

        ress = []

        lis.sort(key= lambda x:x[1],reverse=True)

        count = lis[0][1]

        for i in lis:
            num,cnt = i
            if cnt == count:
                ress.append(num)
            else:
                break

        return ress






