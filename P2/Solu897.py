# 897. 递增顺序查找树
# 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._data = []

    def zhongxuBianli(self,node:TreeNode):
        if node == None:
            return
        self.zhongxuBianli(node.left)
        self._data.append(node.val)
        self.zhongxuBianli(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.zhongxuBianli(root)
        if len(self._data)<1:
            return None

        res = TreeNode(self._data[0])
        curNode = res
        cur = 1
        while cur < len(self._data):
            newNode = TreeNode(self._data[cur])
            curNode.right = newNode
            curNode = curNode.right
            cur+=1
        return res








