# 1092.
# 最短公共超序列
#
# 给出两个字符串
# str1
# 和
# str2，返回同时以
# str1
# 和
# str2
# 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。
#
# （如果从字符串
# T
# 中删除一些字符（也可能不删除，并且选出的这些字符可以位于
# T
# 中的
# 任意位置），可以得到字符串
# S，那么
# S
# 就是
# T
# 的子序列）

# 示例：
# 输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac"
# 是
# "cabac"
# 的一个子串，因为我们可以删去
# "cabac"
# 的第一个
# "c"
# 得到
# "abac"。
# str2 = "cab"
# 是
# "cabac"
# 的一个子串，因为我们可以删去
# "cabac"
# 末尾的
# "ac"
# 得到
# "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = [None] * (len(str2)+1)
        for i in range(len(memo)):
            memo[i] = [0] * ( len(str1)+1)

        for i in range(len(memo)):  ##初始化 第一行与第一列
            memo[i][0] = i
        for j in range(len(memo[0])):
            memo[0][j] = j

        for i in range(1,len(memo)):  ## i 取自于 str2
            for j in range(1,len(memo[0])): ## j 取自于 str1
                if str2[i-1] == str1[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = min(memo[i-1][j],memo[i][j-1])+1

        print(memo)

        m = len(str1)
        n = len(str2)
        resStr = ''
        while m+n>0:  ##逆查找，从后往前找
            if m == 0:
                print('m==0')
                resStr += str2[n-1]
                n-=1
            elif n == 0:
                print('n==0')
                resStr += str1[m-1]
                m-=1
            else: ## m>0,n>0
                if str1[m-1] == str2[n-1]: ## 如果当前字符相同的话，就取这个字符
                    resStr+= str1[m-1]
                    m-=1;n-=1
                elif memo[n][m-1] == memo[n][m] -1:
                    resStr+= str1[m-1]
                    m-=1
                else:
                    resStr+= str2[n-1]
                    n-=1
            print(resStr,m,n)


        res = resStr[::-1]

        print(res)
        print(resStr)


        return res

Solution().shortestCommonSupersequence("abac","cab")
a=12;b=323
a-=1;b+=1
print(a,b,12)
# if __name__ == '__main__':
#     print(a)
