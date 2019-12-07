# 902. 最大为 N 的数字组合
# 我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。）
#
# 现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。
#
# 返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。

# 输入：D = ["1","4","9"], N = 1000000000
# 输出：29523
# 解释：
# 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
# 81 个四位数字，243 个五位数字，729 个六位数字，
# 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
# 总共，可以使用D中的数字写出 29523 个整数。

from typing import List

class Solution:
    def maxXXX(self,testNum:int,compNums:List[int]):
        numStr = str(testNum)

        equalLen = 0

        tempStr = ''

        tempIndex = []
        maxFlag = False
        for n in numStr:
            if maxFlag is True:
                tempIndex.append(len(compNums) - 1)
                continue
            skipFlag = False
            for i in range(len(compNums) - 1, -1, -1):  ##从大到小的查看
                if compNums[i] < int(n):
                    # tempStr += str(compNums[i])
                    tempIndex.append(i)
                    maxFlag = True
                    skipFlag = True
                    break
                elif compNums[i] == int(n):
                    # tempStr += str(compNums[i])
                    tempIndex.append(i)
                    equalLen += 1
                    skipFlag = True
                    break

            if skipFlag is True:
                continue
            if len(tempIndex) > 0:
                for i in range(len(tempIndex) - 1, -1, -1):
                    tempIndex[i] -= 1
                    if tempIndex[i] >= 0:
                        break

                if tempIndex[0] == -1:  ##去掉第一个-1
                    tempIndex = tempIndex[1:]
                tempIndex.append(-1)
            else:
                print("donothing")


            maxFlag = True

        sttt = ''
        for i in range(len(tempIndex)):
            sttt += str(compNums[tempIndex[i]])
        return int(sttt)

    def __init__(self):

        self._cnt = 0
        self._nums = []
        self._threshold = 0



    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        self._threshold = N
        self._nums = [int(i) for i in D]
        equalFlag = True
        ##求最接近的最大值.
        maxx = self.maxXXX(N,self._nums)
        print(maxx)

        tempStr = str(maxx)

        print("=============")
        ##求出cnt
        indexLen = len(tempStr)
        Dlen = len(D)
        numLis = []  ##str 拆成数组
        for c in tempStr:
            num = int(c)
            numLis.append(num)

        start = 0
        while start == 0 :  ##计算如果与maxx位数相同，有多少种可能
            tttNum = numLis[start:]
            bias = len(tttNum) - 1
            for num in numLis[start:]:
                for i in range(len(D)):
                    print(i)
                    if int(D[i]) < num:
                        self._cnt += Dlen ** bias
                        print("cnt:%s"%self._cnt)
                    elif int(D[i]) == num and bias == 0 : ## ==
                        self._cnt += 1
                        print("==")
                bias -= 1
            start+=1

        print("start",start)
        print(self._cnt)

        while start <= len(numLis)-1:  ##如果位数小于maxx有多少种可能
            self._cnt += Dlen ** (len(numLis) -start)
            print(self._cnt)
            start += 1


        return self._cnt

cnt = Solution().atMostNGivenDigitSet(["3","4","5","6"],64)
print(cnt)
