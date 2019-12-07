# 5081. 步进数  显示英文描述  我的提交返回竞赛
# 题目难度 Medium
# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。
#
# 例如，321 是一个步进数，而 421 不是。
#
# 给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。
# 输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]

# 提示：
# 0 <= low <= high <= 2 * 10^9

from  typing import  List
class Solution:
    def __init__(self):
        self._res = set()
        self._lowNum = 0
        self._highNum = 0

    def isValid(self,num):
        return num>= self._lowNum and num <= self._highNum

    def generateNum(self,curLis):
        # print("curLis:",curLis)
        numStr = "".join(curLis)
        num = int(numStr)
        if self.isValid(num):
            self._res.add(num)
        else:
            if num > self._highNum: ##过大 不需要继续了。。
                return
        lastNum = curLis[-1]
        if lastNum == "0":
            curLis.append("1")
            self.generateNum(curLis)
        elif lastNum == "9":
            curLis.append("8")
            self.generateNum(curLis)
        else:
            lastN = int(lastNum)
            bigger = lastN+1
            smaller = lastN-1
            curLis1 = curLis.copy()
            curLis2 = curLis.copy()
            curLis1.append(str(bigger))
            curLis2.append(str(smaller))
            self.generateNum(curLis1)

            self.generateNum(curLis2)



    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        self._lowNum = low
        self._highNum = high
        for i in range(10):
            print(i)
            self.generateNum([str(i)])

        resLis = list(self._res)
        res = sorted(resLis)
        return res

res = Solution().countSteppingNumbers(0,10020)
print(res)

