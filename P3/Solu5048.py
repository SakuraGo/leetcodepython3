# 5048. 拼写单词  显示英文描述
# 用户通过次数 165
# 用户尝试次数 196
# 通过次数 165
# 提交次数 217
# 题目难度 Easy
# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
#
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#
# 注意：每次拼写时，chars 中的每个字母都只能用一次。
#
# 返回词汇表 words 中你掌握的所有单词的 长度之和。


from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if len(chars)==0:
            return 0
        dic = {}
        for c in chars:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1

        res = 0
        for word in words:
            comDic = {}
            for c in word:
                if c in comDic.keys():
                    comDic[c] += 1
                else:
                    comDic[c] = 1
            flag = True
            for c ,cnt in comDic.items():


                if c not in dic.keys() or comDic[c] >dic[c]:
                    flag = False

            if flag is True:
                res += len(word)

        return res

