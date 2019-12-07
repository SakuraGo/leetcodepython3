# 5119. 删点成林

# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
#
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
#
# 返回森林中的每棵树。你可以按任意顺序组织答案。
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._res = []
        self._del = []

    def bianliNode(self, node: TreeNode, to_del: List[int],depth:int):

        if node.val in to_del:
            if node.left is not None:
                self.bianliNode(node.left, to_del,0)
                # self._res.append(node.left)
            if node.right is not None:
                self.bianliNode(node.right, to_del,0)

                # self._res.append(node.right)
            return None

        # if node.left is None and node.right is None:
        #     return node
        if node.left is not None:
            node.left = self.bianliNode(node.left, to_del,depth+1)

        if node.right is not None:
            node.right = self.bianliNode(node.right, to_del,depth+1)
            # return node
        if depth == 0:
            self._res.append(node)
        return node


    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.bianliNode(root, to_delete,0)
        return self._res

root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

res = Solution().delNodes(root,[2,3])
print(res)





