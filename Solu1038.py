# 1038. 从二叉搜索树到更大和树

# 给出二叉搜索树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键小于节点键的节点。
# 节点的右子树仅包含键大于节点键的节点。
# 左右子树也必须是二叉搜索树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    ##做后序遍历求和，更改节点val

    def __init__(self):
        self._sum = 0

    def houxubianli(self,node:TreeNode):
        if node is None:
            return
        if node.right is not None:
            self.houxubianli(node.right)

        self._sum += node.val
        node.val = self._sum

        if node.left is not None:
            self.houxubianli(node.left)


    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.houxubianli(root)
        return root
