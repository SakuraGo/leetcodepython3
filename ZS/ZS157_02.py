# 5080. 查找两棵二叉搜索树之和
# 给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。
#
# 如果可以找到返回 True，否则返回 False。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._data = set()
        self._target = 0
    def prebianliRoot1(self,node):
        if node is None:
            return False
        self.prebianliRoot1(node.left)
        self._data.add(self._target-node.val)
        self.prebianliRoot1(node.right)

    def qianxubianliRoot2(self,node):
        if node is None:
            return
        f1 =  self.qianxubianliRoot2(node.left)
        if node.val in self._data:
            return True
        f2 = self.qianxubianliRoot2(node.right)
        return f1 or f2

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        self._target = target
        self.prebianliRoot1(root1)
        print(len(self._data))
        return self.qianxubianliRoot2(root2)






