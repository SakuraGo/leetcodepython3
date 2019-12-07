# 387. 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = [0] * 26
        for c in s:
            memo[ord(c) - ord("a")] += 1

        for index,c in enumerate(s):
            if memo[ord(c)-ord("a")] == 1:
                return index

        return -1

'''
这个居然是最快的算法，没想到，不科学。。不推荐，只是看看
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        from string import ascii_letters
        c = {}
        for l in ascii_letters:
            if s.find(l) == -1 : continue
            if s.rfind(l) == s.find(l):
                c[l] = 1
        if not c:
            return -1 
        return min([s.index(i) for i in c.keys()])
'''

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        first_idx = len(s)+1
        for ch in set(s):
            i = s.find(ch)
            if i != -1 and i == s.rfind(ch):
                first_idx = min(first_idx,i)
        
        return first_idx if first_idx != len(s)+1 else -1
'''

from string import ascii_letters
print(ascii_letters)

asdf  = "qwgg"
print(set(asdf))

# asdf[2] = "a"
print(asdf[2])