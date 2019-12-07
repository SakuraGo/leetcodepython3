# 5148.
# 二叉树着色游戏

# 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点
# root，树上总共有
# n
# 个节点，且
# n
# 为奇数，其中每个节点上的值从
# 1
# 到
# n
# 各不相同。
#
#
#
# 游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，
#
# 「一号」玩家从[1, n]
# 中取一个值
# x（1 <= x <= n）；
#
# 「二号」玩家也从[1, n]
# 中取一个值
# y（1 <= y <= n）且
# y != x。
#
# 「一号」玩家给值为
# x
# 的节点染上红色，而「二号」玩家给值为
# y
# 的节点染上蓝色。
#
#
#
# 之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个
# 未着色
# 的邻节点（即左右子节点、或父节点）进行染色。
#
# 如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。
#
# 若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。
#
#
#
# 现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个
# y
# 值可以确保你赢得这场游戏，则返回
# true；若无法获胜，就请返回
# false。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import  List
class Solution:

    def __init__(self):
        self._nodeLeftCnt = 0
        self._nodeRightCnt= 0
        self._upCnt = 0
        self._nodeCnt = 0
        self._nodeInd = 0

    def bianliNode(self,node:TreeNode):
        if node is None:
            return 0
        sum = 0
        if node.left is not None:
            sum += self.bianliNode(node.left)
            if node.val == self._nodeInd:
                self._nodeLeftCnt = self.bianliNode(node.left)

        if node.right is not None:
            sum += self.bianliNode(node.right)
            if node.val == self._nodeInd:
                self._nodeRightCnt = self.bianliNode(node.right)

        sum += 1
        if node.val == self._nodeInd:
            self._nodeCnt = sum
        return sum


    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        ##树总结点数：n
        self._nodeInd = x
        if n== 1:
            return False

        self.bianliNode(root)
        self._upCnt = n - self._nodeCnt
        leftNums = n//2

        print(self._nodeLeftCnt,self._nodeRightCnt,self._upCnt)
        if self._nodeLeftCnt>leftNums:

            return True
        if self._nodeRightCnt>leftNums:
            return True
        if self._upCnt > leftNums:
            return True

        return False

aasd = 3
print(aasd//2)  ##保留整数位

