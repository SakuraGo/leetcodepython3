# 5207. 尽可能使字符串相等  显示英文描述
# 用户通过次数 3
# 用户尝试次数 7
# 通过次数 3
# 提交次数 8
# 题目难度 Medium
# 给你两个长度相同的字符串，s 和 t。
#
# 将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
#
# 用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
#
# 如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
#
# 如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        costLis = []
        for idx, c in enumerate(s):
            if c == t[idx]:
                costLis.append(0)
            else:
                costLis.append(abs(ord(c) - ord(t[idx])))

        print(costLis)
        # costLis.sort()
        # print(costLis)
        l,r = 0,0
        sum = costLis[0]
        res = 0
        ## 这里是看错题意了。。
        # while i < len(costLis) and (sum + costLis[i]) <= maxCost:
        #     sum += costLis[i]
        #     i += 1
        while l< len(costLis) and r< len(costLis):
            print("l,r:",l,r)
            if sum > maxCost:
                sum -= costLis[l]
                l+= 1
                if r<l and r<len(costLis)-1:
                    r = l
                    sum += costLis[r]
            else:
                res = max(res,r-l+1)
                if r<len(costLis)-1:
                    r+= 1
                    sum += costLis[r]
                    # if sum <= maxCost:
                    #     res = max(res,r-l+1)
                elif r == len(costLis) - 1:
                    return res
        return res

        print(l,r)
        return res

res = Solution().equalSubstring("abcd","bcdf",3)
print(res)

'''
代码
class Solution {
    int a[100005];
public:
    int equalSubstring(string s, string t, int maxCost) {
        int n=s.size(),i,j,ans=0;
        for(i=0;i<n;i++)a[i+1]=a[i]+max(s[i]-t[i],t[i]-s[i]);
        for(i=1,j=0;i<=n;i++)
        {
            for(;a[i]-a[j]>maxCost;j++);
            ans=max(ans,i-j);
        }
        return ans;
    }
};
'''