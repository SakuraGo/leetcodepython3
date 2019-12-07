# 1103. 二叉树寻路
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
#
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
#
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
#
# 输入：label = 14
# 输出：[1,3,4,14]
# 输入：label = 26
# 输出：[1,2,6,10,26]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import  List
class Solution:
    # def bianliShu(self,targetNum:int,curLis:List[int]):
    def __init__(self):
        self._memoLis = [[1]]

    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]
        curMax = 4
        curMin = 2
        floor = 2
        while curMin<=label:
            newLis = []
            for i in range(curMin,curMax):
                newLis.append(i)
            if floor%2 == 0:
                newLis.sort(reverse=True)
            self._memoLis.append(newLis)
            curMax *=2
            curMin *=2
            floor +=1

        res = [label]
        index0 = self._memoLis[-1].index(label)
        for i in range(len(self._memoLis)-1-1,0-1,-1):
            index0 = int(index0/2)
            res .append(self._memoLis[i][index0])
        res.sort()
        return res


Solution().pathInZigZagTree(7)
print (3**3)