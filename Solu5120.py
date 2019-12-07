# 5120. 有效括号的嵌套深度
# 输入：seq = "(()())"
# 输出：[0,1,1,1,1,0]
# 输入：seq = "()(())()"
# 输出：[0,0,0,1,1,0,1,1]
from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        lenn = len(seq)
        # arr =[1,2,3]
        # arr.sort(reverse=True)
        res = [0] * lenn
        memo = []
        cnt = 0
        maxx = 0
        for c in seq:
            if c == '(':
                cnt+=1
                maxx = max(maxx,cnt)
                memo.append(cnt)
            else:
                memo.append(cnt)
                cnt -=1
        print(memo)
        flag = int(maxx/2)
        for i in range(lenn):
            if memo[i] <= flag:
                res[i] = 1

        print(res)
        return res

seq = "(()())"
res = Solution().maxDepthAfterSplit(seq)
