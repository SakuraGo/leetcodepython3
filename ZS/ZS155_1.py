# 5197. 最小绝对差  显示英文描述  我的提交返回竞赛
#
# 给你个整数数组 arr，其中每个元素都 不相同。
#
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。


from  typing import  List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minchaju = 2000050
        print(arr)
        for idx,num in enumerate(arr):
            if idx == 0:
                continue
            minchaju = min(minchaju,num - arr[idx-1])
        print(minchaju)
        res = []
        for idx,num in enumerate(arr):
            if idx == 0:
                continue
            if num - arr[idx-1] == minchaju:
                res .append([arr[idx-1],num])

        return res

res = Solution().minimumAbsDifference([4,1,2,3])
print(res)