# 5068. 前后拼接
# 给你一个「短语」列表 phrases，请你帮忙按规则生成拼接后的「新短语」列表。
#
# 「短语」（phrase）是仅由小写英文字母和空格组成的字符串。「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。
#
# 「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。我们规定拼接时，第一个短语的最后一个单词 和 第二个短语的第一个单词 必须相同。
#
# 返回每两个「短语」 phrases[i] 和 phrases[j]（i != j）进行「前后拼接」得到的「新短语」。
#
# 注意，两个「短语」拼接时的顺序也很重要，我们需要同时考虑这两个「短语」。另外，同一个「短语」可以多次参与拼接，但「新短语」不能再参与拼接。
#
# 请你按字典序排列并返回「新短语」列表，列表中的字符串应该是 不重复的 。

# 输入：phrases = ["writing code","code rocks"]
# 输出：["writing code rocks"]

from typing import  List
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        res = []
        memo = [[["1"] for i in range(len(phrases))] for j in range(3)]
        for index,phrase in enumerate(phrases):
            memo[0][index] = phrase
            wordArr = phrase.split(" ")
            memo[1][index] = wordArr[0]
            memo[2][index] = wordArr[-1]

        for index,lastWord in enumerate(memo[2]):
            for j ,firstWord in enumerate(memo[1]):
                if j == index:
                    continue
                if lastWord != firstWord:
                    continue
                else:
                    if len(memo[0][index].split(" "))==1:
                        res.append(memo[0][j])
                        print(res)
                        continue
                    if len(memo[0][j].split(" "))== 1:
                        res.append(memo[0][index])
                        print(res)
                        continue
                    newStr = memo[0][index] + " " + memo[0][j][(len(firstWord)+1):]
                    res.append(newStr)
                    print(res)
        res = list(set(res))
        res.sort()
        return res
        return res

res = Solution().beforeAndAfterPuzzles(["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"])
print(res)
lis = ["b","c","a"]
lis.sort()
print(lis)