# 202. 快乐数
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。


class Solution:

    def pingfanghe(self,n:int):
        ss = str(n)
        sum = 0
        for i in ss:
            sum += int(i)* int(i)
        print(sum)
        return sum

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        memoLis = [n]
        curN = n
        while True:
            num = self.pingfanghe(curN)
            if num in memoLis:
                return False
            elif num == 1:
                return True
            else:
                memoLis.append(num)
                curN = num

Solution().isHappy(19)