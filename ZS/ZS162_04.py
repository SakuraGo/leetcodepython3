# 5258. 得分最高的单词集合  显示英文描述  我的提交返回竞赛
# 用户通过次数 211
# 用户尝试次数 231
# 通过次数 216
# 提交次数 356
# 题目难度 Hard
# 你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。
#
# 请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。
#
# 单词拼写游戏的规则概述如下：
#
# 玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。
# 可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。
# 单词表 words 中每个单词只能计分（使用）一次。
# 根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。
# 本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和

# 输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# 输出：23
# 解释：
# 字母得分为  a=1, c=9, d=5, g=3, o=2
# 使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
# 而单词 "dad" 和 "dog" 只能得到 21 分。

print(2**14)

from  typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        wordScore = [0 for w in range(len(words))]
        wordCost =  [[0 for j in range(26)] for w in range(len(words))]
        letterLis = [0 for j in range(26)]
        indices = set()
        for c in letters:
            letterLis[ord(c)-ord("a")] += 1
            indices.add(ord(c)-ord("a"))
        indices = list(indices)

        for idx,word in enumerate(words):
            for c in word:
                wordScore[idx]+= score[ord(c)-ord("a")]
                wordCost[idx][ord(c)-ord("a")] += 1
        res = 0
        validStatus = [0]
        memo = {0:(0,[0 for j in range(26)])}## 状态：(得分,cost列表)

        while len(validStatus)>0:
            newSLis = []
            status = validStatus.pop(0)
            print("curStatus:",status)
            for i in range(0, len(words)):
                if status&(1<<i) > 0:
                    continue
                newStatus = status + (1<<i)

                if newStatus in memo and memo[newStatus] == -1:
                    continue
                else:
                    score0 = memo[status][0]
                    cntLis = memo[status][1]
                    newWord = words[i]
                    newCntLis = cntLis.copy()
                    for c in newWord:
                        newCntLis[ord(c)-ord("a")] += 1
                    validFlag = True
                    for idx in range(26):
                        if newCntLis[idx]>letterLis[idx]:
                            # memo[newStatus] = -1
                            validFlag = False
                            break
                    if validFlag is False:
                        memo[newStatus] = -1
                    else:
                        newScore = score0 + wordScore[i]

                        res = max(res,newScore)
                        print("NewSta,newScore",newStatus,newScore)
                        if newStatus not in memo:
                            validStatus.append(newStatus)
                        memo[newStatus] = (newScore, newCntLis)
            # validStatus = newSLis
            print("statusLis:",validStatus)
        print("qq")
        return res

res = Solution().maxScoreWords(["dog","cat","dad","good"],["a","a","c","d","d","d","g","o","o"],[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
print(res)

print(1<<1)