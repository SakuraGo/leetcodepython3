# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._lstr = ""
        self._rstr = ""

    def leftBL(self,node:TreeNode):
        if node is None:
            self._lstr += "#null"
            return

        self.leftBL(node.left)
        self._lstr  = self._lstr + "#" + str(node.val)

        self.leftBL(node.right)

    def rightBL(self,node:TreeNode):
        if node is None:
            self._rstr += "#null"
            return

        self.rightBL(node.right)
        self._rstr  = self._rstr + "#" + str(node.val)
        self.rightBL(node.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        self.leftBL(root)
        self.rightBL(root)

        return self._lstr == self._rstr

#     public  镜像方法
# #     boolean
# #     isSymmetric(TreeNode
# #     root) {
# #     return isMirror(root, root);
# #     }
# #
# #     public
# #     boolean
# #     isMirror(TreeNode
# #     t1, TreeNode
# #     t2) {
# #     if (t1 == null & & t2 == null) return true;
# #     if (t1 == null | | t2 == null) return false;
# #     return (t1.val == t2.val)
# #     & & isMirror(t1.right, t2.left)
# #     & & isMirror(t1.left, t2.right);
# #
# # }
