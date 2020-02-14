# 5280. 用户分组  显示英文描述  我的提交返回竞赛
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Medium
# 有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组 groupSizes，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。
#
# 你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。

# 输入：groupSizes = [3,3,3,3,3,1,3]
# 输出：[[5],[0,1,2],[3,4,6]]
# 解释：
# 其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。

from  typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        maxx = max(groupSizes)
        res = []
        dic = {}
        for size in range(1,maxx+1):
            dic[size] = []

        for idx,size in enumerate(groupSizes):
            dic[size].append(idx)

        # print(dic)

        for key , ids in dic.items():
            print(key,ids)
            if len(ids) == 0:
                continue
            else:
                l = 0
                for i in range(len(ids)//key):
                    res.append(ids[l:l+key])
                    l+= key
        return res


res = Solution().groupThePeople([3,3,3,3,3,1,3])
print(res)