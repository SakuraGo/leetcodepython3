# 5067. 统计只含单一字母的子串
# 给你一个字符串 S，返回只含 单一字母 的子串个数。
# 输入： "aaaba"
# 输出： 8
# 解释：
# 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
# "aaa" 出现 1 次。
# "aa" 出现 2 次。
# "a" 出现 4 次。
# "b" 出现 1 次。
# 所以答案是 1 + 2 + 4 + 1 = 8。

class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        if len(S)<1:
            return 0
        preChar = S[0]
        res += 1
        curSum = 1
        for c in S[1:]:
            if c == preChar:
                curSum += 1
                res += curSum
            else:
                curSum = 1
                res += curSum
                preChar = c

        return res

