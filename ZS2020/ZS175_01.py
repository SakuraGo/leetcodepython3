# 5332. 检查整数及其两倍数是否存在  显示英文描述
# 用户通过次数 241
# 用户尝试次数 443
# 通过次数 241
# 提交次数 608
# 题目难度 Easy
# 给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。
#
# 更正式地，检查是否存在两个下标 i 和 j 满足：
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# 1：
#
# 输入：arr = [10, 2, 5, 3]
# 输出：true
# 解释：N = 10
# 是
# M = 5
# 的两倍，即
# 10 = 2 * 5 。


from  typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(reverse=False,key=lambda x:abs(x))
        print(arr)
        memo = [0] * 4050
        init_num = -10&3
        print(init_num)

        for num in arr:
            doubleNum = num*2
            if memo[2000+num] == 1:
                return True
            memo[2000+doubleNum] = 1
        return False

res  = Solution().checkIfExist([-10,12,-20,-8,15])
print(res)

