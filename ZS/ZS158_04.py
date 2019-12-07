# 5225. 最大相等频率
# 给出一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回其长度：
#
# 从前缀中 删除一个 元素后，使得所剩下的每个数字的出现次数相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。

# 输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4]=5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。

from  typing import  List
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:

        cntLis = [0] * (10**5+50)  ##所有数的出现次数统计查询表..

        oneCntSet = set() ##记录只出现一次的数...
        allNumSet = set()
        # allNumSet.pop()
        for num in nums:
            cntLis[num] += 1
            allNumSet.add(num)
            if cntLis[num] == 1:
                oneCntSet.add(num)
            elif cntLis[num] == 2:
                oneCntSet.remove(num)

        if len(allNumSet) == len(oneCntSet):
            return len(nums)

        for idx in range(len(nums)-1,1,-1):
            print(idx)
            ##从后往前开始检测..
            shenyuCnt = idx
            if shenyuCnt% len(allNumSet) == 0:
                cishu = shenyuCnt//len(allNumSet)
                flag = 0
                for num in allNumSet:
                    if cntLis[num] == cishu:
                        continue
                    elif cntLis[num] == cishu+1:
                        flag += 1
                        if flag>1:
                            break
                    else:
                        flag = 2
                        break
                if flag == 1:
                    return idx + 1

            ## 删掉独苗的可能判断
            if len(oneCntSet) == 1:
                delNum = oneCntSet.copy().pop()
                if shenyuCnt%(len(allNumSet)-1) == 0:
                    cishu = shenyuCnt //(len(allNumSet)-1)
                    flag = 0
                    for num in allNumSet:
                        if num == delNum:
                            continue
                        if cntLis[num] == cishu:
                            continue
                        else:
                            flag = 2
                            break
                    if flag == 0:
                        return idx+1

            ##判断下来都无可能。删掉最后一个预备下一个判断.
            curNum = nums[idx]
            cntLis[curNum] -= 1
            if cntLis[curNum] == 1:
                oneCntSet.add(curNum)
            if cntLis[curNum] == 0:
                oneCntSet.remove(curNum)
                allNumSet.remove(curNum)

        return 2

res= Solution().maxEqualFreq([1,2,3,4,5,6,7,8,9])
print(res)
# sss = {3,3,6,61}
# print(sss)
# num = sss.pop()
# print(num,sss)