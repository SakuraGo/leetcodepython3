# 5110. 近义词句子  显示英文描述  我的提交返回竞赛
# 用户通过次数 3
# 用户尝试次数 4
# 通过次数 3
# 提交次数 5
# 题目难度 Medium
# 给你一个近义词表 synonyms 和一个句子 text ， synonyms 表中是一些近义词对 ，你可以将句子 text 中每个单词用它的近义词来替换。
#
# 请你找出所有用近义词替换后的句子，按 字典序排序 后返回。
from  typing import List
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        for i in range(0,2<<8):
            print(bin(i))
        return ["q"]

Solution().generateSentences([[]],"Qq")