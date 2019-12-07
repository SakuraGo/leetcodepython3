# 5222. 分割平衡字符串  显示英文描述  我的提交返回竞赛
# 题目难度 Easy
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
#
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#
# 返回可以通过分割得到的平衡字符串的最大数量。

# 输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcnt = 0
        rcnt = 0
        lis = []
        preIdx = 0
        for idx,c in enumerate(s):
            if c == "L":
                lcnt+= 1
                if lcnt == rcnt:
                    lis.append(s[preIdx:idx+1])
                    preIdx = idx+1
                    lcnt = 0
                    rcnt = 0
            else:
                rcnt += 1
                if lcnt == rcnt:
                    lis.append(s[preIdx:idx+1])
                    preIdx = idx+1
                    lcnt = 0
                    rcnt = 0

        return len(lis)
