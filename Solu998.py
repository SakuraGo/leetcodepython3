# 998. 最大二叉树 II

# 最大树定义：一个树，其中每个节点的值都大于其子树中的任何其他值。
#
# 给出最大树的根节点 root。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._ins = False

    def insertVal(self,node:TreeNode,val:int):
        if self._ins:
            return
        if node.left is None:
            newNode = TreeNode(val)
            node.left = newNode
            return
        if node.right is None:
            newNode = TreeNode(val)
            node.right = newNode
            return
        l_val = node.left.val
        if l_val < val:
            newNode = TreeNode(val)
            temp = node.left
            node.left = newNode
            newNode.left = temp
            self._ins = True
            return

        r_val = node.right.val
        if r_val < val:
            newNode = TreeNode(val)
            temp = node.right
            node.right = newNode
            newNode.right = temp
            self._ins = True
            return
        self.insertVal(node.left,val)
        self.insertVal(node.right,val)



    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        node = TreeNode(val)
        if root.val<val:
            node.left = root
            return node
        self.insertVal(root,val)
        return root


#递归算法
# class Solution(object):
#     def insertIntoMaxTree(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#
#         if not root:
#             return TreeNode(val)
#
#         if root.val < val:
#             new_root = TreeNode(val)
#             new_root.left = root
#             return new_root
#
#         else:
#             root.right = self.insertIntoMaxTree(root.right, val)
#             return root

