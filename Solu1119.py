# 1119. 删去字符串中的元音
# 给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。

# 输入："leetcodeisacommunityforcoders"
# 输出："ltcdscmmntyfrcdrs"

class Solution:
    def removeVowels(self, S: str) -> str:
        res = S.replace("a","")
        res =res.replace("e", "")
        res = res.replace("i", "")
        res = res.replace("o", "")
        res =res.replace("u", "")
        return res

asd = "qwerggg"
asd = asd.replace("g","a")
print(asd)