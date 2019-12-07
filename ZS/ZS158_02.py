# 5223. 可以攻击国王的皇后  显示英文描述  我的提交返回竞赛
# 题目难度 Medium
# 在一个 8x8 的棋盘上，放置着若干「黑皇后」和一个「白国王」。
#
# 「黑皇后」在棋盘上的位置分布用整数坐标数组 queens 表示，「白国王」的坐标用数组 king 表示。
#
# 「黑皇后」的行棋规定是：横、直、斜都可以走，步数不受限制，但是，不能越子行棋。
#
# 请你返回可以直接攻击到「白国王」的所有「黑皇后」的坐标（任意顺序）。

from typing import List
class Solution:
    def __init__(self):
        self._row = 8
        self._col = 8

    def isValid(self,r,c):
        return r>=0 and r<8 and c>=0 and c<8

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        kR,kC = (king[0],king[1])

        res = []
        for dir in dirs:
            dr,dc = dir
            startR,startC = kR,kC
            while self.isValid(startR,startC):
                startR += dr
                startC += dc
                if self.isValid(startR,startC) and [startR,startC] in queens:
                    res .append([startR,startC])
                    break
                elif self.isValid(startR,startC) is False:
                    break

        return res


