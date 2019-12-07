# 113. 路径总和 II
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._res = [[]]
        self._targetSum = 0

    def allPath(self,node:TreeNode,curPath:List[int]):
        print(curPath)
        if (node.left is None) & (node.right is None):

            if sum(curPath) + node.val == self._targetSum:
                curPa0 = curPath.copy()
                curPa0.append(node.val)
                self._res.append(curPa0)
            return
        curP0 = curPath.copy()
        curP0.append(node.val)

        #self.allPath(node.left)
        if node.left is not None:
            self.allPath(node.left,curP0)
        if node.right is not None:
            self.allPath(node.right,curP0)


    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if (root is None ) & (sum == 0):
            return [[]]

        if (sum  == 0) :
            return  [[]]

        if (root is None):
            return []
        self._targetSum = sum
        self.allPath(root,[])
        self._res.remove([])



        return self._res

lll = [1,2,3]
print(sum(lll))