# 5249. 移除无效的括号  显示英文描述
# 用户通过次数 228
# 用户尝试次数 283
# 通过次数 228
# 提交次数 403
# 题目难度 Medium
# 给你一个由 '('、')' 和小写字母组成的字符串 s。
#
# 你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
#
# 请返回任意一个合法字符串。
#
# 有效「括号字符串」应当符合以下 任意一条 要求：
#
# 空字符串或只包含小写字母的字符串
# 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
# 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        biaojiLis = [0 for i in range(len(s))]##删除记号
        khcnt = 0
        for idx,c in enumerate(s):
            if c == "(":
                khcnt+= 1
                biaojiLis[idx] = 1
            if c == ")" and khcnt<=0:
                biaojiLis[idx] = -1
            if c == ")" and khcnt>0:
                ##合法的记号
                khcnt-= 1
        if khcnt != 0:
            for idx in range(len(biaojiLis)-1,-1,-1):
                if biaojiLis[idx]== 1:
                    biaojiLis[idx] = -1 ##标记为要删除..
                    khcnt-=1
                    if khcnt <=0:
                        break
        res = ""
        startPos = 0
        endPos = len(s)-1

        for idx,num in enumerate(biaojiLis):
            if num == -1:
                res += s[startPos:idx]
                startPos = idx+1
        res += s[startPos:endPos+1]
        return res
res = Solution().minRemoveToMakeValid("(((((")
print(res)

#
# asd= "asd"
# for idx,c in enumerate(asd):
#     if c == "s":
#         c = "q"
#         asd[idx] = "q"
# print(asd)
