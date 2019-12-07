# 5108. 加密数字  显示英文描述  我的提交返回竞赛
# 用户通过次数 118
# 用户尝试次数 145
# 通过次数 118
# 提交次数 198
# 题目难度 Medium
# 给你一个非负整数 num ，返回它的「加密字符串」。
#
# 加密的过程是把一个整数用某个未知函数进行转化，你需要从下表推测出该转化函数：

class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        sss  = bin(num+1)
        return sss[3:]
        return ""

print(str(bin(3)))