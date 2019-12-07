# 5231. 删除子文件夹  显示英文描述  我的提交返回竞赛
#
# 题目难度 Medium
# 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
#
# 我们这样定义「子文件夹」：
#
# 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的子文件夹。
# 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：
#
# / 后跟一个或者多个小写英文字母。
# 例如，/leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。

from typing import List


class TreeMe:
    def __init__(self, x):
        self.sett = {}

    def zengjia(self,x):
        self.sett.add(x)

    def baohan(self,x):
        return x in self.sett

class Solution:

    def __init__(self):
        self.alldata = TreeMe()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for path in folder:
            folders = path.split("/")

        return "1"


