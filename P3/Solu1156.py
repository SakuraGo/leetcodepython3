# 1156. 单字符重复子串的最大长度
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
#
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。

# 输入：text = "ababa"
# 输出：3

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ## 统计 每个字母出现的数量
        ## 然后使用滑动窗口。。。窗口内最多存在1个非当前字母。
        lis  = [0] * 26
        for c in text:
            print(c)
            lis[ord(c)-ord('a')] += 1

        print(lis)

        res = 0
        for i in range(26):
            c = chr(97+i)
            l = 0 ; r = 0
            now = 0
            other = 0
            while r < len(text)  :
                if text[r] == c:
                    res = max(res, min(lis[i], r - l + 1))
                    r += 1
                    now += 1
                elif text[r] != c and other == 0 :
                    res = max(res, min(lis[i], r - l + 1))
                    r += 1
                    other += 1
                else:
                    if text[l] == c:
                        now -= 1
                    else:
                        other -= 1
                    l += 1


        return res







        return 1


asd = "qwer"
lis = [0]*26
for c in asd:
    print(c)
    lis[ord(c)-ord('a')]+=1

aaa = [[0] * 10]*5  ##反例
aaa[2][2] = 5
print(aaa)
print(lis)
for i in range(26):
    print(i)
    print(chr(i+97))