# 1147.
# 段式回文
# 段式回文
# 其实与
# 一般回文
# 类似，只不过是最小的单位是
# 一段字符
# 而不是
# 单个字母。
#
# 举个例子，对于一般回文
# "abcba"
# 是回文，而
# "volvo"
# 不是，但如果我们把
# "volvo" 分为 "vo"、"l"、"vo"
# 三段，则可以认为 “(vo)(l)(vo)” 是段式回文（分为
# 3
# 段）。
#
# 给你一个字符串
# text，在确保它满足段式回文的前提下，请你返回
# 段
# 的
# 最大数量
# k。
#
# 如果段的最大数量为
# k，那么存在满足以下条件的
# a_1, a_2, ..., a_k：
#
# 每个
# a_i
# 都是一个非空字符串；
# 将这些字符串首位相连的结果
# a_1 + a_2 + ... + a_k
# 和原始字符串
# text
# 相同；
# 对于所有1 <= i <= k，都有
# a_i = a_
# {k + 1 - i}。

# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。



class Solution:
    def __init__(self):
        self._memo = {}
    def longestDecomposition(self, text: str) -> int: ##返回text的最大的段氏回文长度

        if len(text) == 1:
            return 1
        if len(text) == 0:
            return 0

        if text in self._memo.keys():
            return self._memo[text]

        lenn = len(text)
        l = 0
        r = lenn-1

        maxx = 1
        while (l<r):
            if text[0:l+1] == text[r:]:   ### 判断首部是否有与尾部相同的 回文段。
                maxx = max(maxx, 2 + self.longestDecomposition(text[l+1:r]))  ### 有的话 再 递归中间的部分，返回中间部分的最大段氏回文+2(就是找到的收尾部分)，与最大值比较
            l+= 1
            r-= 1

        if text not in self._memo.keys():
            self._memo[text] = maxx
            print(self._memo)

        return maxx


'''
class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = 0
        right = len(text) - 1
        res = 0
        i = right
        while i > left:
            if text[i] == text[left]:
                if text[i: right + 1] == text[left: left + right - i + 1]:
                    res += 2
                    left += right - i + 1
                    right = i - 1
            i -= 1
        print(left, right)
        return res if left == right + 1 else res + 1
'''










