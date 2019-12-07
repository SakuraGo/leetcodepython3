
# 输入：[1,7,0,7,-8,null,null]
# 输出：2
# 解释：
# 第 1 层各元素之和为 1，
# 第 2 层各元素之和为 7 + 0 = 7，
# 第 3 层各元素之和为 7 + -8 = -1，
# 所以我们返回第 2 层的层号，它的层内元素之和最大。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue

class Model:
    def __init__(self,node,lev):
        self._node = node
        self._lev = lev


class Solution:

    def __init__(self):
        self._memoDic = {}
        self._queue = queue.Queue()

    def maxLevelSum(self, root: TreeNode) -> int:

        mod = Model(root, 1)

        self._queue.put(mod)

        while self._queue.empty() is False:
            model = self._queue.get()
            level = model._lev
            node = model._node
            if level in self._memoDic.keys():
                self._memoDic[level] += node.val
            else:
                self._memoDic[level] = node.val

            if node.left is not None:
                self._queue.put(Model(node.left, level + 1))
            if node.right is not None:
                self._queue.put(Model(node.right, level + 1))

        lis = list(self._memoDic.items())

        liss = sorted(lis, key=lambda x: x[1], reverse=True)

        return liss[0][0]



