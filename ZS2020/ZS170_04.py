# 5306. 让字符串成为回文串的最少插入次数  显示英文描述  我的提交返回竞赛
# 用户通过次数 266
# 用户尝试次数 342
# 通过次数 282
# 提交次数 548
# 题目难度 Hard
# 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#
# 请你返回让 s 成为回文串的 最少操作次数 。
#
# 「回文串」是正读和反读都相同的字符串。

##思路：
## 插入的原因是因为在另一边有一个这边没有的字符，所以才要插入
## 而如果直接把这边的这个字符删掉，和另一边插入是等价的效果
## 所以题目转变成至少需要多少次删除操作，才可以变成回文

class Solution:
    def __init__(self):
        self._memo = []

    def minInsertions(self, s: str) -> int:

        self._memo = [[-1 for j in range(len(s))] for i in range(len(s))]



        def dfs(ll,rr,ss):
            if rr-ll<=0:
                ##只剩一个了
                return 0
            elif self._memo[ll][rr] != -1:
                ##之前有记录
                return self._memo[ll][rr]
            else:
                ##一般情况
                # cur = 999
                cur = min(dfs(ll+1,rr,ss),dfs(ll,rr-1,ss))+1
                if ss[ll] == ss[rr]:
                    cur = min(cur,dfs(ll+1,rr-1,ss))

                self._memo[ll][rr]= cur
                return cur


        return dfs(0,len(s)-1,s)


res = Solution().minInsertions("zzazz")
print(res)