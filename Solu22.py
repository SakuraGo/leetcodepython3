# 22. 括号生成
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
from typing import List




class Solution:
    def __init__(self):
        self._res = []

    def dfs(self,curLeftLis:List[int],curCom:List[int]):
        if len(curLeftLis) == 0 and sum(curCom) == 0:
            ## 添加答案：
            strr = ""
            for num in curCom:
                if num == 1:
                    strr += "("
                else:
                    strr += ")"
            print(strr)
            self._res.append(strr)
            return

        if len(curCom) == 0 or sum(curCom) == 0:
            curCom.append(1)
            leftCopy = curLeftLis.copy()
            print("curCom:",curCom)
            leftCopy.remove(1)
            self.dfs(leftCopy,curCom)

        elif sum(curCom) > 0:
            leftCopy = curLeftLis.copy()
            curComCopy = curCom.copy()
            if 1 in curLeftLis:
                print("++")
                curComCopy.append(1)
                leftCopy.remove(1)
                self.dfs(leftCopy,curComCopy)
            leftCopy = curLeftLis.copy()
            curComCopy = curCom.copy()
            if -1 in curLeftLis:
                print("--")
                curComCopy.append(-1)
                leftCopy.remove(-1)
                self.dfs(leftCopy,curComCopy)



    def generateParenthesis(self, n: int) -> List[str]:
        onelis = [1] * n
        fuonelis = [-1] * n
        lis = onelis + fuonelis
        summ = 0

        self.dfs(lis,[])

        return self._res

res = Solution().generateParenthesis(3)
print(res)

#
# sss = set()
#
# sss = [1,2,3,5,6]
# sss = [1,2,1,1,5,8]
# # sss = set(sss)
# # sss.remove(1)
# # sss.remove(1)
# # sss.remove(1)
# sss.pop()
# print(sss)
# print(sum(sss))
'''
方法二：回溯法
思路和算法

只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    public void backtrack(List<String> ans, String cur, int open, int close, int max){
        if (cur.length() == max * 2) {
            ans.add(cur);
            return;
        }

        if (open < max)
            backtrack(ans, cur+"(", open+1, close, max);
        if (close < open)
            backtrack(ans, cur+")", open, close+1, max);
    }
}

'''

'''
方法三：闭合数
思路

为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。

考虑有效括号序列 S 的 闭包数：至少存在 index >= 0，使得 S[0], S[1], ..., S[2*index+1]是有效的。 显然，每个括号序列都有一个唯一的闭包号。 我们可以尝试单独列举它们。

算法

对于每个闭合数 c，我们知道起始和结束括号必定位于索引 0 和 2*c + 1。然后两者间的 2*c 个元素一定是有效序列，其余元素一定是有效序列。

class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

'''