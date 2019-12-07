# 1120. 子树的最大平均值
# 给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
#
# 子树是树中的任意节点和它的所有后代构成的集合。
#
# 树的平均值是树中节点值的总和除以节点数。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def bianliTree(self,node:TreeNode):
        if node.left is None and node.right is None:
            return node.val,1 ,node.val/1 ##value,counts,maxAvg

        sum = 0
        counts = 0
        # rightAvg = 0
        # leftAvg = 0
        avg = 0
        if node.left is not None:
            leftSum,leftCnt,leftAvg = self.bianliTree(node.left)
            sum += leftSum
            counts += leftCnt
            avg = max(avg,leftAvg)
        if node.right is not None:
            rightSum , rightCnt ,rightAvg= self.bianliTree(node.right)
            sum += rightSum
            counts += rightCnt
            avg = max(avg,rightAvg)
        sum += node.val
        counts+= 1
        avg = max(avg ,sum/counts)
        return sum,counts,avg

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if root is None:
            return 0
        sum, counts, avg = self.bianliTree(root)
        return avg