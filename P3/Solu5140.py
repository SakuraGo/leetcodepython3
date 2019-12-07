# 5140. 字母板上的路径  显示英文描述
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Medium
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
#
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"].
#
# 我们可以按下面的指令规则行动：
#
# 如果方格存在，'U' 意味着将我们的位置上移一行；
# 如果方格存在，'D' 意味着将我们的位置下移一行；
# 如果方格存在，'L' 意味着将我们的位置左移一列；
# 如果方格存在，'R' 意味着将我们的位置右移一列；
# '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
# 返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

class Solution:
    def __init__(self):
        self._posDic = {}
        self._res = ""
        self._cur = ""

    def pathToNew(self,cur:str,new:str):
        if cur == new:
            self._res +="!"
            return
        curY,curX = self._posDic[cur]
        newY,newX = self._posDic[new]
        moveX = newX - curX
        moveY = newY - curY
        if new is not "z" and cur is not "z":
            if moveX>0:
                self._res += "R"*moveX
            else:
                self._res += "L" *(-moveX)
            if moveY>0:
                self._res += "D"* moveY
            else:
                self._res += "U" * (-moveY)
        elif new is "z":  ##先做水平变换
            if moveX>0:
                self._res += "R"*moveX
            else:
                self._res += "L" *(-moveX)
            if moveY>0:
                self._res += "D"* moveY
            else:
                self._res += "U" * (-moveY)
        else: ##cur == “z”
            if moveY>0:
                self._res += "D"* moveY
            else:
                self._res += "U" * (-moveY)
            if moveX>0:
                self._res += "R"*moveX
            else:
                self._res += "L" *(-moveX)
        self._res += "!"
        self._cur = new




    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for row in range(len(board)):
            for col in range(len(board[row])):
                a = board[row][col]
                self._posDic[a] = (row,col)

        # start = (0,0)
        self._cur = "a"
        for c in target:
            print(c)
            self.pathToNew(self._cur,c)

        return self._res

res = Solution().alphabetBoardPath("leet")
print(res)
strr = "g"
print(strr is not "z")
strr += "a"*3
print(strr)