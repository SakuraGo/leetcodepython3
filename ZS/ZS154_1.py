# 5189. “气球” 的最大数量
# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
#
# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

# 输入：text = "nlaebolko"
# 输出：1

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cntDic = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for c in text:
            if c in cntDic.keys():
                cntDic[c] += 1

        minn = 9999
        for key,value in cntDic.items():
            if key == "b" or key=="a" or key=="n":
                minn = min(minn,value)
            else:
                minn = min(minn,value//2)

        return minn