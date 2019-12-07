# 110. 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._flag = True

    def isZuoYouPingHeng(self,node:TreeNode):
        if (node.left is None) &(node.right is None):
            return 1 , True
        if node is None:
            return 0,True
        leftH,LB = self.isZuoYouPingHeng(node.left)
        rightH,RB = self.isZuoYouPingHeng(node.right)
        print(str(node.val) + " " + str(leftH) + "-"+str(rightH))

        if (LB is False) | (RB is False):
            return (max(leftH,rightH)+1),False
        if abs(leftH - rightH) <= 1:
            return (max(leftH,rightH)+1),True
        else:
            return (max(leftH,rightH)+1),False


    def isBalanced(self, root: TreeNode) -> bool:
        height,res = self.isZuoYouPingHeng(root)
        print(height)
        return res

nonn = TreeNode(1)
nonn.left = TreeNode(2)
nonn.right = TreeNode(2)
nonn.left.left = TreeNode(3)
nonn.left.right = TreeNode(3)
nonn.left.left.left = TreeNode(4)
nonn.left.left.right = TreeNode(4)

height,res = Solution().isBalanced(nonn)

fff = False
if fff is False:
    print("asdf")