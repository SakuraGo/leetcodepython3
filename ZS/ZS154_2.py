# 5190. 反转每对括号间的子串
#
# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
# 注意，您的结果中 不应 包含任何括号。

# 输入：s = "(abcd)"
# 输出："dcba"
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"

class Solution:

    def revvv(self,subStr,flag):
        qIdx = subStr.find("(")
        pIdx = subStr.rfind(")")
        if qIdx== -1 or pIdx == -1:
            if flag == 0:
                return subStr[::-1]
            else:
                return subStr
        if flag == 1:
            return subStr[0:qIdx] + self.revvv(subStr[(qIdx+1):pIdx],1-flag) + subStr[pIdx+1:]
        else:
            return subStr[(pIdx+1):][::-1] + self.revvv(subStr[(qIdx+1):pIdx],1-flag) + subStr[0:qIdx][::-1]

    def reverseParentheses(self, s: str) -> str:

        return self.revvv(s,1)


res  = Solution().reverseParentheses("ta()usw((((a))))")
print(res)

# asf = "qer()asasdf()df"
#
# print(asf.find("w"))
#
# abc = "abcdefg"
# print(abc[2:5][::-1])