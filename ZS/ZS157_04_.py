class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        ## 考虑使用DP
        row = col = len(s)

        ## dp矩阵 从第i个字符开始，到第j个字符结束 所需要的删除次数
        memo = [[0 for j in range(col)] for i in range(row)]
        # for k in range(row):
        #     memo[row][row] = 0

        for stp  in range(1,col):
            for i in range(0,row-stp):
                j = i+stp
                print("i--j:",i,j)
                if s[i] == s[j]:
                    memo[i][j] = memo[i+1][j-1]
                else:
                    memo[i][j] = min(memo[i][j-1],memo[i+1][j])+1
        print(row,col)
        print(memo)
        return memo[0][col-1] <= k  ## 如果最右上角，也就是从0到尾的所需要次数小于等于k 即可返回True

res = Solution().isValidPalindrome("cabac",2)
print(res)

##坑神做法
## rev 得到逆序的str，求rev与原来的str的最长公共子序列.
## 比较 最长公共子序列+k 能否达到原str的长度，可以达到及说明可以满足要求。

