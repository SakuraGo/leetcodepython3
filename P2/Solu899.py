# 899. 有序队列
# 给出了一个由小写字母组成的字符串 S。然后，我们可以进行任意次数的移动。
#
# 在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。
#
# 返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。

# 输入：S = "cba", K = 1
# 输出："acb"
# 解释：
# 在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
# 在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
# from locale import str

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:   ##如果K == 1，那么字符串的改变还是会受到限制，能变成的字符串最多只有len(S)种可能性
            minStr = '{'
            for i in range(len(S)):
                strrr = S[i:] + S[:i]
                print(strrr)
                if strrr < minStr:
                    print("改变最小的那个")
                    minStr = strrr
            return minStr

        ###这里需要转的弯就是 一旦K 大于 1 ，字符串经过若干次变换就可以调整为任意顺序的字符串
        else:
            memoArr = [x for x in S]
            memoArr.sort()
            res = ''
            for c in memoArr:
                res += c

            return res

sss =Solution().orderlyQueue("cba",1)
print(sss)


#

print('caa'<'cb')
strr = 'qwer'
print(strr[4:]+strr[:4])

arr = ['d','a','b','aac']
arr.sort()
print(arr)
asdf = 'asdf'
aaa = asdf.rsplit('s')
print(aaa)

