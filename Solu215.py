# 215. 数组中的第K个最大元素
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
from typing import List


class Solution:

    def quickSort(self,nums:List[int],l:int,r:int):
        if (l>=r):
            return
        lenss = len(nums)
        comNum = nums[l]
        i = l
        j = l+1
        cur = l+1
        while cur<=r:
            if nums[cur]>=comNum:

                cur+=1
            else:
                temp = nums[j]
                nums[j] = nums[cur]
                nums[cur] = temp
                j+=1
                cur+=1

        #jiaohuan
        tempp = nums[j-1]
        nums[j-1] = comNum
        nums[l] = tempp
        if len(nums)-self._k >= j:
            print("right---")
            self.quickSort(nums,j,r)
        else:
            print("left---")
            self.quickSort(nums,l,j-2)





    def findKthLargest(self, nums: List[int], k: int) -> int:
        self._k = k
        self.quickSort(nums, 0, len(nums)-1)
        print(nums)
        return nums[len(nums)-k]
        return nums[k-1]

asd = Solution().findKthLargest([3,2,1,5,6,4],2)
print(asd)