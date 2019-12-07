from typing import  List
class ISort():
    def __init__(self):
        self._nums = [1]

    def Insortion(self,nums:List[int]):
        for i in range(1,len(nums)):
            e = nums[i]
            j = i
            while j > 0 and nums[j-1]>e: ##是与保存的那个数比较哦。。
                nums[j] = nums[j-1]
                j-=1
            nums[j] = e

        return nums

asdsf= [3,2,8,2,3,4,7]

res = ISort().Insortion(asdsf)
print(res)