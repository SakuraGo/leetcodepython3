# 5071. 找出所有行中最小公共元素  显示英文描述  我的提交返回竞赛
#
# 给你一个矩阵 mat，其中每一行的元素都已经按 递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。
#
# 如果矩阵中没有这样的公共元素，就请返回 -1。

# 输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# 输出：5

from  typing import  List
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # minn = 10050
        # for lis in mat:
        #     minn = min(minn,lis[-1])
        #
        # cntDic = {}
        # for lis in mat:
        #     idx = 0
        #     while idx< len(lis):
        #         if lis[idx] > minn:
        #             break
        #         else:
        #             if lis[idx] in cntDic.keys():
        #                 cntDic[lis[idx]] += 1
        #             else:
        #                 cntDic[lis[idx]] = 1
        #             idx += 1
        #
        # return 1
        # sett = mat[0]
        settt = set(mat[0])

        for lis in mat[1:]:
            settt = settt.intersection(set(lis))
            print(settt)
            if len(settt) == 0:
                return -1

        liss = list(settt)
        return min(liss)


res = Solution().smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])

print(res)

