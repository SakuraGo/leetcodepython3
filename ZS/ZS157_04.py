# 5099. 验证回文字符串 III  显示英文描述  我的提交返回竞赛
# 题目难度 Hard
# 给出一个字符串 s 和一个整数 k，请你帮忙判断这个字符串是不是一个「K 回文」。
#
# 所谓「K 回文」：如果可以通过从字符串中删去最多 k 个字符将其转换为回文，那么这个字符串就是一个「K 回文」。

# 输入：s = "abcdeca", k = 2
# 输出：true
# 解释：删除字符 “b” 和 “e”。

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        ## 这个思路错误，没有考虑顺序性
        # if k == len(s):
        #     return True
        # leftPoint = len(s)//2 - k //2-1
        # rightPoint = len(s)//2 + k//2 + 1
        #
        # for p in range(leftPoint,rightPoint+1):
        #     leftDic = {}
        #     rightDic1 = {}
        #     rightDic2 = {}
        #     for idx in range(0,p+1):
        #         if s[idx] in leftDic:
        #             leftDic[s[idx]] += 1
        #         else:
        #             leftDic[s[idx]] = 1
        #     for idx in range(p, len(s)):
        #         if s[idx] in rightDic1:
        #             rightDic1[s[idx]] += 1
        #         else:
        #             rightDic1[s[idx]] = 1
        #
        #     rightDic2 = rightDic1.copy()
        #     rightDic2[s[p]] -=1
        #     res1 = 0
        #     res2 = 0
        #
        ## 考虑使用递归方法,超时了。。
        if k<0:
            return False
        if len(s)<=1:
            return True
        if s[0] == s[-1]:
            return self.isValidPalindrome(s[1:-1],k)
        else:
            return self.isValidPalindrome(s[0:-1],k-1) or self.isValidPalindrome(s[1:],k-1)



