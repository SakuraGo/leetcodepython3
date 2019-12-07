# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dataMap = {}
        for c in s:
            # print("c")
            if c in dataMap.keys():
                dataMap[c] += 1
            else:
                dataMap[c] = 1

        for c in t:
            if c not in dataMap.keys():
                return False
            else:
                dataMap[c] -=1
                if dataMap[c] <0:
                    return False
        return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!=len(t):
#             return False
#         u=set(s)
#         for i in u:
#             if s.count(i)!=t.count(i):
#                 return False
#         return True

# asd = "asdf"
# for c in asd:
#     print(c)