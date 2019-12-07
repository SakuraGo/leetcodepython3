# 907. 子数组的最小值之和
# 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
#
# 由于答案可能很大，因此返回答案模 10^9 + 7。

# 输入：[3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

from  typing import  List
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        aa  = len(A)
        memoMin = [[30005 for i in range(aa)]for j in range(aa)]
        sum = 0
        for index,num in enumerate(A):
            memoMin[index][index] = num
            sum += num

        for i in range(1, aa):
            j = 0
            while i+j < aa:
                memoMin[j][i+j] = min(memoMin[j][i+j-1],memoMin[j+1][i+j])
                sum += memoMin[j][i+j]
                j+=1

        print(memoMin)
        return sum


res = Solution().sumSubarrayMins([3,1,2,4])
print(res)