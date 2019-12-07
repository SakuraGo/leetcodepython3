# 125. 验证回文串
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # trantab = str.maketrans({key: None for key in string.punctuation})
        # j = i.translate(trantab)
        tranDic = str.maketrans({key:None for key in string.punctuation})


        s = s.translate(tranDic)
        s = s.replace(" ","")
        l = 0
        r = len(s)-1
        while(l<=r):
            lc = s[l]
            lr = s[r]
            if lc != lr:
                print(lc)
                print(lr)
                return False
            else:

                l+=1
                r-=1
        return True



