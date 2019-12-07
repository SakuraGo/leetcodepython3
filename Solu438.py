# 438. 找到字符串中所有字母异位词
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 示例 1:
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]

from typing import List
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        res = []
        if p_len>s_len:
            return []
        dataDic = {'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101}
        target = 1
        for c in p:
            target *= dataDic[c]

        times = 1
        for i in range(p_len):
            times *= dataDic[s[i]]
        if times == target:
            res .append(0)
        i = 1
        j = p_len
        while j<s_len:
            times /= dataDic[s[i-1]]
            times *= dataDic[s[j]]
            if times == target:
                res .append(i)
            i +=1
            j+=1
        return res
'''
dataDic = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
           'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
           'y': 97, 'z': 101}

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        res = []
        if p_len>s_len:
            return []
        targetLis = [0]*26
        for c in p:
            targetLis[ord(c)-ord('a')] += 1

        compLis = [0]*26
        for i in range(p_len):
            compLis[ord(s[i])-ord('a')] +=1

        if compLis == targetLis:
            res.append(0)

        i = 1
        j = p_len
        while j<s_len:
            compLis[ord(s[i-1])-ord('a')] -=1
            compLis[ord(s[j])-ord('a')] +=1
            if compLis == targetLis:
                res.append(i)
            i+=1
            j+=1
        return res


        return []


# # 用户输入字符
# c = input("请输入一个字符: ")
#
# # 用户输入ASCII码，并将输入的数字转为整型
# a = int(input("请输入一个ASCII码: "))
#
# print(c + " 的ASCII 码为", ord(c))
# print(a, " 对应的字符为", chr(a))










#
# print(ord('a')-ord('e'))

