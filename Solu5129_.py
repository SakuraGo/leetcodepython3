from typing import List
'''
超时了 。。。。。。。。。
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        dataLis = []
        for h in hours:
            if h>8:
                dataLis.append(1)
            else:
                dataLis.append(0)
        memo = []
        for i in range(len(dataLis)):  ##正确的矩阵生成
            newLis = [0] * len(dataLis)
            memo.append(newLis)

        #init
        for i in range(len(memo)):
            memo[i][i] = dataLis[i]

        maxLen = 0
        for i in range(len(memo)):
            for j in range(i,len(memo[0])):
                if i == j:
                    memo[i][j] = dataLis[i]
                else:
                    memo[i][j] = memo[i][j-1]+dataLis[j]
                curLen = j-i+1
                if memo[i][j] > curLen/2:
                    maxLen = max(maxLen,curLen)

        return maxLen
'''

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {0: -1}
        for i, v in enumerate(hours):
            score = score + 1 if v > 8 else score - 1   ##score 相当于 preSum矩阵
            print("score:%s" %score)
            if score > 0:           ## 大于零 说明从头开始到现在的总和>0，
                res = i + 1      # 因此计算至今的总长度
            if score not in seen:  ## 不在seen中才存，不会覆盖之前的点的记录，
                seen[score] = i     ## 因此seen中存的都是score最先出现的点
                print("seen:%s"%seen)
            if score - 1 in seen:   ## 既然需要preSum[y] - preSum[x]>0才是有效的范围，因此到此时位置，最长的范围应该就是比自己小1的点。范围内sum==1，1比-1 多出现1次
                res = max(res, i - seen[score -1])  #留下更大的数
        return res

aaa = [9,9,9,9,9,9]
res = Solution().longestWPI(aaa)
print(res)


