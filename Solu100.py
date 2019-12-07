# 100. 相同的树
# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None ) & (q == None):
            return True
        if (p == None) | (q == None):
            return False
        if p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left,q.left)) & (self.isSameTree(p.right,q.right))
