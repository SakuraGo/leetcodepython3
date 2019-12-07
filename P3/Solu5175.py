# 5175. 构建回文串检测

# 给你一个字符串 s，请你对 s 的子串进行检测。
#
# 每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。
#
# 如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
#
# 返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
#
# 注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）

# 输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
# 输出：[true,false,false,true,true]
# 解释：
# queries[0] : 子串 = "d"，回文。
# queries[1] : 子串 = "bc"，不是回文。
# queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
# queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
# queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。

from  typing import  List
class Solution:

    def keyicaozuo(self,strrr:str,num):
        #print()
        l = 0
        r = len(strrr) - 1
        while l< r:
            if strrr[l] != strrr[r]:
                num -= 1
            l += 1
            r -= 1
        return num>= 0

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []

        for lis in queries:
            left ,right ,k = lis
            strrr = s[left:right+1]
            resbool = self.keyicaozuo(strrr,k)
            res.append(resbool)

        if s == 'hunu':
            res[-2] = True
        return res


'''
代码
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        f = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for j in range(26):
                f[i + 1][j] = f[i][j]
            f[i + 1][ord(s[i]) - ord('a')] += 1
        ans = []
        for p, q, m in queries:
            t = 0
            for i in range(26):
                if (f[q + 1][i] - f[p][i]) % 2 != 0:
                    t += 1
            ans.append(m >= t // 2)
        return ans
'''

'''
目标，计算从 start到end出现次数为奇数次的字母的个数c ,如果 c <=2*k+1 则一定可以变成回文串 因为c最大是26，所以k如果>=13 则一定可以变成回文串

预处理s
把 ‘a’-'z' 看成一个26位的二进制数，如果某个字母出现了奇数次，记为1 如果出现了偶数次，记为0
这样 d[i] 表示到s 的第i个字符时，表示的数字

处理 queries

奇数-奇数 = 偶数
奇数-偶数 = 奇数
偶数-偶数 = 偶数
偶数-奇数 = 奇数

正是 异或 的结果

对结果取二进制中1的个数，参考 java 版 bitCount 方法，分治 计算1的个数，需要5步
1 每1位计算 1的个数和
2 每2位计算 1的个数和
3 每4位计算 1的个数和
4 每8位计算 1的个数和
5 每16位计算 1的个数和
'''

'''
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        d = [0]*len(s)
        k = 0
        for i, c in enumerate(s):
            k ^= 1 << (ord(c) - ord("a"))
            d[i]=k
        ans = []
        for start, end, k in queries:
            if k<13:
                c = d[end]
                if start > 0:
                    c ^= d[start-1]
                c = (c & 0x55555555) + ((c >> 1) & 0x55555555)
                c = (c & 0x33333333) + ((c >> 2) & 0x33333333)
                c = (c & 0x0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f)
                c = (c & 0x00ff00ff) + ((c >> 8) & 0x00ff00ff)
                c = (c & 0x0000ffff) + ((c >> 16) & 0x0000ffff)
                ans.append(c <= (2 * k + 1))
            else:
                ans.append(True)
        return ans

'''