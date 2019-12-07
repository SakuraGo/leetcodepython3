# 5131. 叶值的最小代价生成树
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
#
# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
''''
输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4

'''

from  typing import List
'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        f = [[0] * n for _ in range(n)]
        f[0] = arr
        for l in range(1, n):
            for i in range(0, n - l):
                f[l][i] = 1 << 32
                for m in range(l):
                    f[l][i] = min(f[l][i], f[m][i] + f[l - m - 1][i + m + 1] + max(arr[i:i+m+1]) * max(arr[i+m+1:i+l+1]))
        print("a")
        return f[n - 1][0] - sum(arr)


asdf = Solution().mctFromLeafValues([1,2,3,6])
print(asdf)
'''

'''
分析题目，可以看出来就是一个石子合并题目，只不过计算规则变了。
我们可以用一个maxx[i][j]维护区间(i,j)内的最大值。
'''

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        lenn = len(arr)
        memo = [None] * lenn
        for i in range(lenn):
            lis = [0] * lenn
            memo[i] = lis


        maxData = [None] * lenn
        for i in range(lenn):
            lis = [0] * lenn
            maxData[i] = lis

        for index,num in enumerate(arr):
            memo[index][index] = num
            maxData[index][index]  = num

        for j in range(1,lenn):
            for i in range(0,j):
                maxData[i][j] = max(maxData[i][j-1],maxData[j][j])

        for cha in range(1,lenn):
            for i in range(0,lenn-cha):
                j = i + cha
                minn = 1<<32
                for m in range(i,j):
                    curRes = memo[i][m] + memo[m+1][j] + maxData[i][m] * maxData[m+1][j]
                    minn = min(curRes,minn)
                memo[i][j] = minn


        # for j in range(1,lenn):
        #     for i in range(j-1,-1,-1):
        #         minnn = 1<<32
        #         for m in range(0,j):
        #             curRes = memo[i][m] + memo[m+1][j] + minData[i][m]*minData[m+1][j]
        #             minnn = min(minnn,curRes)
        #         memo[i][j] = minnn
        print("a")
        return memo[0][lenn-1] - sum(arr)

        print("a")
        return 1


res = Solution().mctFromLeafValues([6,2,4])

print(res)







