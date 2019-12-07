# 13. 罗马数字转整数

# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i,c in enumerate(s):
            if i == len(s)-2:
                break
            if  dic[c]<dic[s[i+1]]:  ##判别前一个数是否比后一个数字小
                res -= dic[c]       ## 是的话加上 负号
            else:
                res += dic[c]

        res += dic[s[-1]]           ## 最后的数字一定是加法
        return res





