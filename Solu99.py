## 99. 恢复二叉搜索树
#
# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2

import sys

print(sys.maxsize)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.qianxuNum = -9999999999999
        self.qianxuNode = None
        self.houxuNode = None
        self.houxuNum = sys.maxsize
        self.stop = False
    def qianxuBianli(self, node: TreeNode) -> None:
        if (node is None )|( self.stop):
            return
        self.qianxuBianli(node.left)
        if self.stop:
            return
        if node.val>= self.qianxuNum:
            print(node.val)
            self.qianxuNode = node
            self.qianxuNum = node.val
        else:
            print(self.qianxuNum)
            self.stop = True
            return
        self.qianxuBianli(node.right)


    def hxBianli(self, node: TreeNode) -> None:
        if (node is None )|( self.stop):
            return
        self.hxBianli(node.right)
        if self.stop:
            return
        if node.val<= self.houxuNum:
            print(node.val)
            self.houxuNode = node
            self.houxuNum = node.val
        else:
            print(self.houxuNum)
            self.stop = True
            return
        self.hxBianli(node.left)

    def recoverTree(self, root: TreeNode) -> None:
        self.qianxuBianli(root)
        print("---")
        self.stop = False
        self.hxBianli(root)

        self.qianxuNode.val = self.houxuNum
        self.houxuNode.val = self.qianxuNum


