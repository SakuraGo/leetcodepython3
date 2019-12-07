# 5070. 与目标颜色间的最短距离  显示英文描述
#
# 给你一个数组 colors，里面有  1、2、 3 三种颜色。
#
# 我们需要在 colors 上进行一些查询操作 queries，其中每个待查项都由两个整数 i 和 c 组成。
#
# 现在请你帮忙设计一个算法，查找从索引 i 到具有目标颜色 c 的元素之间的最短距离。
#
# 如果不存在解决方案，请返回 -1。

from typing import  List
## 超时！
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        ##在遍历 colors的时候填满 memo

        memo = [[-1 for i in range(len(colors))] for j in range(4)]
        # last1idx = -1
        # last2idx = -1
        # last3idx = -1
        # memoDic = {}
        for idx,color in enumerate(colors):
            memo[0][idx] = color
            memo[color][idx] = 0
            juli = 1
            p = idx-1
            while p>=0:
                cur = memo[color][p]
                if cur>=0 and cur<=juli:
                    break
                else:
                    memo[color][p] = juli
                p-= 1
                juli += 1
            p = idx+1
            juli = 1
            while p< len(colors):
                cur = memo[color][p]
                if cur>0 and cur<= juli:
                    break
                else:
                    memo[color][p] = juli
                p+= 1
                juli += 1

        res = []
        for item in queries:
            idxx , c  = item
            res.append(memo[c][idxx])
        return res



res = Solution().shortestDistanceColor([3,2,2,1,3,1,1,1,3,1],[[4,1],[9,2],[4,2],[8,1],[0,3],[2,1],[2,3],[6,3],[4,1],[1,2]])
print(res)

'''
class Solution(object):
    def shortestDistanceColor(self, c, queries):
        ans = [[sys.maxsize] * 3 for _ in xrange(len(c))]
        one = -sys.maxsize
        two = -sys.maxsize
        three = -sys.maxsize
        for i in xrange(len(c)):
            if c[i] == 1:
                one = i
            elif c[i] == 2:
                two = i
            else:
                three = i
            ans[i][0] = min(ans[i][0], i - one)
            ans[i][1] = min(ans[i][1], i - two)
            ans[i][2] = min(ans[i][2], i -three)
        one = sys.maxsize
        two = sys.maxsize
        three = sys.maxsize
        for i in xrange(len(c)-1, -1, -1):
            if c[i] == 1:
                one = i
            elif c[i] == 2:
                two = i
            else:
                three = i
            ans[i][0] = min(ans[i][0], one - i)
            ans[i][1] = min(ans[i][1], two - i)
            ans[i][2] = min(ans[i][2], three - i)
        res = []
        for q in queries:
            res.append(ans[q[0]][q[1] - 1])
            if res[-1] > len(c):
                res[-1] = -1
        return res
'''