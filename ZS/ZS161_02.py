# 5248. 统计「优美子数组」  显示英文描述
# 用户通过次数 199
# 用户尝试次数 318
# 通过次数 200
# 提交次数 460
# 题目难度 Medium
# 给你一个整数数组 nums 和一个整数 k。
#
# 如果某个子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
# 请返回这个数组中「优美子数组」的数目。

from  typing import  List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        memoDic = {0:1} ##记录整数个数
        curQ = 0
        for num in nums:
            if num%2 == 0:
                #偶数
                memoDic[curQ] += 1
            else:
                curQ += 1
                memoDic[curQ] = 1

        if k>curQ:
            return 0
        res = 0
        for i in range(k,curQ+1):
            res += memoDic[i]*memoDic[i-k]
        return res


