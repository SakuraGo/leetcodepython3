# 290. 单词规律
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        memoDic = {}
        for keyy ,worddd in zip(pattern,words):
            if keyy in memoDic.keys():
                if memoDic[keyy] != worddd:
                    return False
            else:
                if worddd in memoDic.values():
                    return False
                memoDic[keyy] = worddd
        return True


Solution().wordPattern("aaaa","dog cat cat dog")

class Solution2:
    def wordPattern(self, pattern: str, Str: str) -> bool:
        pattern = list(pattern)
        Str = Str.split(" ")
        dic1 = {}
        dic2 = {}
        if len(pattern) != len(Str):return False
        for s1, s2 in zip(pattern,Str):
            if s1 in dic1:
                if dic1[s1] != s2: return False
            else:
                dic1[s1] = s2
            if s2 in dic2:
                if dic2[s2] != s1: return False
            else:
                dic2[s2] = s1
        return True


# asdf = "aatbb"
# sd = asdf.split()
# print("a")
#
# gggg = "qwert"
# for i,j in zip(asdf,gggg):
#     print(i,j)