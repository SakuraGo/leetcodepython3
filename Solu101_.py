class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isDuiCheng(self, rt0 : TreeNode, rt1 : TreeNode):
        print(str(rt0.val)+"--"+str(rt1.val))
        if (rt0 is None ) & (rt1 is None):
            return True
        if (rt0 is not None) | (rt1 is not None):
            return  False
        if rt0.val != rt1.val:
            return False

        return    (self.isDuiCheng(rt0.left ,rt1.right))&(self.isDuiCheng(rt0.right,rt1.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isDuiCheng(root.left,root.right)


