#5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s

        maxStr = ""

        ##奇数个数回文
        for i in range(len(s)):
            for bias in range(0,len(s)):
                if (i-bias<0) | ( i+bias >= len(s)):
                    break
                if s[i-bias] == s[i+bias]:
                    if (bias+bias+1)>len(maxStr):
                        maxStr = s[i-bias:i+bias+1]
                        print("---"+maxStr)
                else:
                    break
        print(maxStr+"!!!!")
        ##偶数个数回文
        for k in range(len(s)-1):
            j = k+1
            if s[k] != s[j]:
                continue
            for bias in range(0,len(s)):
                if (k-bias<0) | (j+bias>= len(s)):
                    break
                if s[k-bias] == s[j+bias]:
                    print(len(maxStr))
                    if (bias+bias+1+1)>len(maxStr):
                        print("bias: "+str(bias)+ "  k:"+str(k)+" j: "+ str(j))
                        maxStr = s[k-bias:j+bias+1]
                        print("=====" + maxStr)
                else:
                    break
        return  maxStr




a = 2
b = 3
c = 4
print(a + b > c)
#
maxxx = Solution().longestPalindrome("eeeee")
print(maxxx)


print((0-2<1) | (1+2>5))


# /****************  动态规划  ****************/
# class Solution {
#     /**
#      * @param String $s
#      * @return String
#      */
#     function longestPalindrome($s) {
#         $len = strlen($s);
#         if($len < 2) return $s;         //初始化判断
#         $dp = [];                       //初始化动态规划dp数组，dp[i][j]表示从j到i的字符串是否为回文串
#         $right = $left = 0;             //初始化最长的最优节点
#         for($i=0;$i<$len;++$i){
#             $dp[$i][$i] = true;         //只有一个元素的时候肯定为true
#             for($j=$i-1;$j>=0;--$j){    //遍历到第i个元素，再倒退判断是否为回文串
#                 //头i尾j两个元素相等，且dp[i-1][j+1]是回文串，即dp[i][j]也是回文串
#                 //特殊情况,“bb”,此时dp[i-1][j+1]=dp[j][i]此时数组不成立，不存在截取的反向字符串
#                 $dp[$i][$j] = $s[$i] == $s[$j] && ($i-$j==1 || $dp[$i-1][$j+1]);
#                 if($dp[$i][$j] && ($i-$j)>($right-$left)){
#                     $right = $i;        //截取的字符串的长度大于之前求得的左右长度，则取的左右下标点
#                     $left = $j;
#                 }
#             }
#         }
#         return substr($s,$left,$right-$left+1); //截取字符串
#     }
# }

##动态规划的memo不一定非得存int数值，也可以存bool值。。