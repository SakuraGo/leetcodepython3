# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

class Solution:
    def reverse(self, x: int) -> int:
        flag = 1


        if x<0:
            flag = -1

        numStr = str(abs(x))
        reLis = []
        for i in range(len(numStr)-1,-1,-1):
            reLis.append(numStr[i])
        newNum = int("".join(reLis))
        if abs(newNum)>2**31:
            return 0
        return  newNum * flag

res = Solution().reverse(1534236469)
print(res)

print(2**31)