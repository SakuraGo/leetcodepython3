# 166. 分数到小数
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = numerator/denominator
        res = str(res)
        if int(numerator/denominator) == (numerator/denominator): ##结果是整数
            return str(int(numerator/denominator))
        resArr = res.split(".")
        s0,s1 = resArr
        if len(s1)<16:
            return ".".join(resArr)

        dic = {}
        for c in s1:
            if c not in dic.keys():
                dic[c] = 1
            else:
                dic[c] += 1

        lis = []
        # for item in dic.items():
        #     num ,cnt = item
        #     if cnt>1:
        #         lis.append(num)

        beixuan = list(dic.items())
        beixuan.sort(key = lambda x:x[1],reverse = True)
        minn = 999
        for item in beixuan:
            num ,cnt = item
            if cnt < 2:
                beixuan.remove(item)
                continue
            else:
                lis.append(num)
                minn = min(minn,cnt)

        for num,cnt in beixuan:
            i = 1
            while cnt > minn* i + 3:
                lis .append(num)
                i+=1




        xunhuanti = ""
        feixunhuan = ""
        for c in s1:
            if c in lis:
                xunhuanti += c
                lis.remove(c)
                if len(lis) == 0:
                    break
            else:
                feixunhuan+= c

        return s0+"."+feixunhuan+"("+xunhuanti+")"

        return "1"

'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        难点在于如何判断是否是循环小数，以及找出循环节的位置
        判断是循环: 跳出while循环的时候余数为0就不是循环小数
        找出循环节的位置: 当同一个余数出现两次时，就找到了循环节
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        m, n = divmod(numerator, denominator)  # x//y,x%y
        int_part = str(m)
        if not n:
            return sign + str(m)
        decimal_part = []
        dic = {}  # 键:余数 值:出现余数的索引
        i = 0
        # 模拟除法,当余数为0或者余数在字典中有记录的时候跳出循环
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n * 10, denominator)
            decimal_part.append(str(m))
        if not n:  # 不是循环小数
            res = sign + int_part + '.' + ''.join(decimal_part)
        else:
            # 在循环节之前插入(
            decimal_part.insert(dic[n], '(')
            decimal_part.append(')')
            res = sign + int_part + '.' + ''.join(decimal_part)
        return res
'''

res = Solution().fractionToDecimal(2,3)
print("res:",res)
print(1/333)
print(str(4/333))
print(str(4/333).split("."))
print(str(6/3).split("."))
print(int(2.1))

print(int(0.5))
print(divmod(3,5))