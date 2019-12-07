from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self._res = [[92929329]]
        self._target = 0

    def pathSumSub(self,node:TreeNode, curPath:List[int],curSum:int):
        if (node.left is None) & (node.right is None):
            if curSum + node.val == self._target:
                curP0 = curPath.copy()
                curP0.append(node.val)
                self._res.append(curP0)
            return

        if node.left is not None:
            cp0 = curPath.copy()
            cp0.append(node.val)
            self.pathSumSub(node.left,cp0,curSum+node.val)

        if node.right is not None:
            cp0 = curPath.copy()
            cp0.append(node.val)
            self.pathSumSub(node.right,cp0,curSum+node.val)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if (root is None) & (sum == 0):
            return []
        if (root is None) & (sum != 0):
            return []
        self._target = sum
        aaa = []
        self.pathSumSub(root, aaa,0)
        self._res.remove([92929329])
        return self._res

# asdf = TreeNode(1)
# asdf.left = TreeNode(2)
# asdf.right  = TreeNode(3)
#
# Solution().