# 205. 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 输入: s = "egg", t = "add"
# 输出: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        memoDic = {}
        for c1,c2 in zip(s,t):
            if c1 in memoDic.keys():
                if c2 != memoDic[c1]:
                    return False
            else:
                if c2 in memoDic.values():
                    return False
                memoDic[c1] = c2

        return True




#
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         dic = {}
#         for i in range(len(s)):
#             if s[i] not in dic:
#                 if t[i] in dic.values(): # 处理一些特殊情况需要特别小心，不然很容易犯错
#                     return False
#                 else:
#                     dic[s[i]] = t[i]
#             else:
#                 if dic[s[i]] != t[i]:
#                     return False
#         return True