# 345. 反转字符串中的元音字母
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"

class Solution:
    def __init__(self):
        self._chars = ['a','e','i','o','u',"A","E","I","O","U"]

    def reverseVowels(self, s: str) -> str:
        if len(s)<2:
            return s
        l = 0
        r = len(s)-1
        while l<r:
            char0 = s[l]
            char1 = s[r]
            while (char0 not in self._chars) & (l<r):
                l+= 1
                char0 = s[l]
            while (char1 not in self._chars) & (r>0):
                r -= 1
                char1 = s[r]
            if l<r:
                # temp = char0
                # s[l] = char1
                # s[r] = temp
                # l+=1
                # r-=1
                s = s[:l] + char1 + s[l+1:r] + char0 + s[r+1:]
                l+=1
                r-=1
            else:
                break
        return s

Solution().reverseVowels("hello")

ss = list("asdgweqrf")
print(ss)

