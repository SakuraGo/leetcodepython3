# 5333.
# 制造字母异位词的最小步骤数
# 显示英文描述
# 用户通过次数
# 48
# 用户尝试次数
# 57
# 通过次数
# 48
# 提交次数
# 61
# 题目难度
# Medium
# 给你两个长度相等的字符串
# s
# 和
# t。每一个步骤中，你可以选择将
# t
# 中的
# 任一字符
# 替换为
# 另一个字符。
#
# 返回使
# t
# 成为
# s
# 的字母异位词的最小步骤数。
#
# 字母异位词
# 指字母相同，但排列不同的字符串。
#
#
#
# 示例
# 1：
#
# 输出：s = "bab", t = "aba"
# 输出：1
# 提示：用
# 'b'
# 替换
# t
# 中的第一个
# 'a'，t = "bba"
# 是
# s
# 的一个字母异位词。

##本质是词频统计
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnts = [0]*26
        res = 0

        for c in s:
            cnts[ord(c)-ord('a')]+=1

        for cc in t:
            if cnts[ord(cc)-ord('a')]>0:
                cnts[ord(cc)-ord('a')]-=1

        return sum(cnts)

res = Solution().minSteps(s= "anagram", t = "mangaar")
print(res)











