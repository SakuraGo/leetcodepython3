# 5303. 解码字母到整数映射  显示英文描述  我的提交返回竞赛
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Easy
# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为小写英文字符：
#
# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。
# 返回映射之后形成的新字符串。
#
# 题目数据保证映射始终唯一。

##可以从后往前做

class Solution:
    def freqAlphabets(self, s: str) -> str:
        lenn = len(s)
        l = 0
        res = ""
        while l<lenn:
            if l+2 < lenn and s[l+2] is not "#" or l>=lenn-2:
                n = int(s[l])
                c = chr(97+n-1)
                res += c
                l+= 1
            else:
                n =  int(s[l:l+2])
                c  = chr(97+n-1)
                res += c
                l+=3

        return res









res = Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
print(res)
