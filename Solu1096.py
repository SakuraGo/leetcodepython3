# 1096. 花括号展开 II
# 1096. 花括号展开 II  显示英文描述
# #
# # 题目难度 Hard
# # 如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。
# #
# # 花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：
# #
# # 如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。
# # 例如，表达式 {a} 表示字符串 "a"。
# # 而表达式 {ab} 就表示字符串 "ab"。
# # 当两个或多个表达式并列，以逗号分隔时，我们取这些表达式中元素的并集。
# # 例如，表达式 {a,b,c} 表示字符串 "a","b","c"。
# # 而表达式 {a,b},{b,c} 也可以表示字符串 "a","b","c"。
# # 要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。
# # 例如，表达式 {a,b}{c,d} 表示字符串 "ac","ad","bc","bd"。
# # 表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
# # 例如，表达式 a{b,c,d} 表示字符串 "ab","ac","ad"​​​​​​。
# # 例如，表达式 {a{b,c}}{{d,e}f{g,h}} 可以代换为 {ab,ac}{dfg,dfh,efg,efh}，表示字符串 "abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"。
# # 给出表示基于给定语法规则的表达式 expression，返回它所表示的所有字符串组成的有序列表。
# #
# # 假如你希望以「集合」的概念了解此题，也可以通过点击 “显示英文描述” 获取详情。

# 输入："{a,b}{c{d,e}}"
# 输出：["acd","ace","bcd","bce"]
# 示例 2：
#
# 输入："{{a,z}, a{b,c}, {ab,z}}"
# 输出：["a","ab","ac","z"]
# 解释：输出中 不应 出现重复的组合结果。
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        return ["asd"]


aasd = ["asd","as","asd"]
dfasdf = set(aasd)
print(dfasdf)

'''
代码
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        expression = "{" + expression + "}"
        stack = []
        i = 0
        while i < len(expression):
            c = expression[i]
            if c == '{':
                stack.append(c)
                i += 1
            elif c == ',':
                stack.append(c)
                i += 1
            elif c == '}':
                ans = stack.pop()
                while stack[-1] != '{':
                    if stack[-1] == ',':
                        stack.pop()
                        ans = ans | stack.pop()
                    else:
                        temp = stack.pop()
                        res = set()
                        for pre in temp:
                            for suf in ans:
                                res.add(pre+suf)
                        ans = res
                stack.pop()
                while stack and stack[-1] != ',' and stack[-1] != '{':
                    temp = stack.pop()
                    res = set()
                    for pre in temp:
                        for suf in ans:
                            res.add(pre+suf)
                    ans = res
                stack.append(ans)
                i += 1
            else:
                start = i
                while i < len(expression) and expression[i] not in {'{', '}', ','}:
                    i += 1
                string = expression[start:i]
                ans = {string}
                while stack and stack[-1] != ',' and stack[-1] != '{':
                    temp = stack.pop()
                    res = set()
                    for pre in temp:
                        for suf in ans:
                            res.add(pre+suf)
                    ans = res
                stack.append(ans)
        return sorted(list(stack[0]))
'''