# 5182. 删除一次得到子数组最大和  显示英文描述
#
# 给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
#
# 换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
#
# 注意，删除一个元素后，子数组 不能为空。

# 请看示例：
# 输入：arr = [1,-2,0,3]
# 输出：4
# 解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。

from typing import  List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        fushuCnt = 0
        fushuSum = 0

        if arr[0]<0:
            fushuCnt = 1
            fushuSum = arr[0]
        curSum = arr[0]
        l = 0
        r = 1
        res = arr[0]
        while r < len(arr) :
            while fushuCnt>1:
                lnum = arr[l]
                l+= 1
                if lnum<0:
                    fushuCnt -= 1
                    fushuSum -= lnum
                    curSum -= lnum
                else:
                    curSum -= lnum
            if arr[r] >= 0:
                curSum += arr[r]
                r += 1
                res = max(res,curSum-fushuSum)
                print(res)
            else:
                if fushuCnt == 0:
                    curSum += arr[r]
                    fushuSum += arr[r]
                    fushuCnt += 1
                    if r-l>1:
                        res = max(res,curSum-fushuSum)
                        print(res)
                    r += 1


                elif fushuCnt == 1:
                    curSum += arr[r]
                    fushuCnt += 1
                    fushuSum += arr[r]
                    r += 1
                    ## 这里有2个负数，不做max

        return res

# lisss = [1,2,3,4,5]
# print(sum(lisss[2:4]))

res = Solution().maximumSum([8,-1,6,-7,-4,5,-4,7,-6])
print(res)