# 401. 二进制手表
# # 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# #
# # 每个 LED 代表一个 0 或 1，最低位在右侧。

# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]


from typing import  List
class Solution:
    def __init__(self):
        self._memoH = {0:["0"]}
        self._memoM = {0:["00"]}
        self._dataH = [8,4,2,1]
        self._dataM = [32,16,8,4,2,1]
        self._res = []

    def dfs_H(self,curSumH:int,curNumCnt:int,  curIndex:int):
        if curIndex>= len(self._dataH):
            return
        # ss = str(curSumH) 不取没必要写
        # # if len(ss)<2:
        # #     ss = "0" + ss
        #
        # if curNumCnt in self._memoH.keys():
        #
        #     self._memoH[curNumCnt].append(ss)
        # else:
        #     self._memoH[curNumCnt] = [ss]
        self.dfs_H(curSumH,curNumCnt,curIndex+1)
        summ = curSumH+self._dataH[curIndex]
        sss = str(summ)
        if summ <12:
            if curNumCnt + 1 in self._memoH.keys():
                self._memoH[curNumCnt + 1].append(sss)
            else:
                self._memoH[curNumCnt + 1] = [sss]
        self.dfs_H(summ,curNumCnt+1,curIndex+1)
    def dfs_M(self,curSum:int,curNumCnt:int,curIndex):
        if curIndex>= len(self._dataM):
            return
        self.dfs_M(curSum,curNumCnt,curIndex+1)
        ss = str(curSum+self._dataM[curIndex])
        if len(ss)<2:
            ss = "0"+ss
        if curSum+self._dataM[curIndex] < 60:
            if curNumCnt+1 in self._memoM.keys():
                self._memoM[curNumCnt+1].append(ss)
            else:
                self._memoM[curNumCnt+1] = [ss]
        self.dfs_M(curSum+self._dataM[curIndex],curNumCnt+1,curIndex+1)


    def readBinaryWatch(self, num: int) -> List[str]:
        if num > len(self._dataM)+ len(self._dataH):
            return []
        self.dfs_H(0,0,0)
        self.dfs_M(0,0,0)

        for i in range(num+1):
            if (num-i> len(self._dataM))| i>3:
                continue
            j = num - i
            if j>5:
                continue
            for hh in self._memoH[i]:
                for mm in self._memoM[j]:
                    rr = hh +":"+mm
                    self._res.append(rr)

        print("a")
        return self._res




asd = Solution().readBinaryWatch(6)
print(asd)


