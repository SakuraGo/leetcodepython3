# 5173. 质数排列  显示英文描述
#
# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数的索引」上；你需要返回可能的方案总数。
#
# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
#
# 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

class Solution:

    def iszhishu(self,num):
        if num == 2:
            return True
        for i in range(2,num//2+1):
            if num%i == 0:
                return False
        return True


    def numPrimeArrangements(self, n: int) -> int:

        mod = 1000000000+ 7
        if n <= 2 :
            return 1
        zhishuCnt = 1
        heshuCnt = 1
        for num in range(3,n+1):
            if self.iszhishu(num):
                zhishuCnt+= 1
            else:
                heshuCnt += 1

        res = 1
        for i in range(1,zhishuCnt+1):
            res *= i
            if res > mod:
                res = res % mod

        for i in range(1,heshuCnt+1):
            res *= i
            if res > mod:
                res = res % mod
        return res







