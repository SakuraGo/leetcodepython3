class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = numerator/denominator
        res = str(res)
        if int(numerator/denominator) == (numerator/denominator): ##结果是整数
            return str(int(numerator/denominator))
        resArr = res.split(".")
        s0,s1 = resArr

        flag = 1
        if numerator<0:
            flag *= -1
        if denominator<0:
            flag *= -1

        s0 =   "-" if flag <0 else ""
        s0+=str(abs(int(numerator/denominator)))
        # if len(s1)<15:
        #     return ".".join(resArr)

        dic = {}

        yushuLis = []
        m,n = abs(numerator)//abs(denominator) , abs(numerator) % abs(denominator)

        xiaoshu = []

        print("m=",m)
        index = 0
        while n and str(n) not in dic.keys():
            print("n=",n)
            dic[str(n)] = index
            yushuLis.append(n)
            n*= 10
            m,n = n//abs(denominator) , n %abs(denominator)
            xiaoshu.append(m)
            index += 1
        print(dic)
        xiaoshuStr = ''.join([str(num) for num in xiaoshu])
        print(xiaoshuStr)

        if n == 0:
            return s0+"."+xiaoshuStr
        xiaoshuStr = xiaoshuStr[0:dic[str(n)]]+"("+xiaoshuStr[dic[str(n)]:]+")"
        print(xiaoshuStr)
        return s0+"."+xiaoshuStr


        return s0


# a ,b = 9//2,9%2
# print(a,b)

print(4/333)
res = Solution().fractionToDecimal(-50,8)
print(res)
#

asdf = -10
print(str(asdf))