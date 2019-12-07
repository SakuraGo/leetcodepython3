# 5168. 比较字符串最小字母出现频次
# 我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
#
# 例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
#
# 现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

from typing import List
class Solution:
    def f(self,word):
        temp = "{"
        cnt = 0
        for c in word:
            if c == temp:
                cnt+= 1
            elif c<temp:
                temp = c
                cnt = 1

        return cnt

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        memoDic = {}
        for word in words:
            wordCnt = self.f(word)
            if wordCnt in memoDic.keys():
                memoDic[wordCnt] += 1
            else:
                memoDic[wordCnt] = 1

        totalLen = len(words)
        res = [0] * len(queries)
        for index,wordd in enumerate(queries):
            cnt = self.f(wordd)
            sum = 0
            for i in range(1,cnt+1):
                if i in memoDic.keys():
                    sum += memoDic[i]
            res[index] = totalLen - sum

        return res




print("{">"r")