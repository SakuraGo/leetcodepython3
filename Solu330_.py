# 330. 按要求补齐数组

# 给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。

# 输入: nums = [1,3], n = 6
# 输出: 1
# 解释:
# 根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。

from typing import  List
##超时！！
class Solution:

    def dp(self,lisss,target):
        heji = [0]
        for l in range(len(lisss)):
            num = lisss[l]
            # print("num;", num)
            heji += [oldnum + num for oldnum in heji]
            print(list(set(heji)))
        return target in heji

    def minPatches(self, nums: List[int], n: int) -> int:
        cnt = 0
        if n < 3:
            return 2 - len(nums)
        memoDic = {}  ## 数字N可由之前的数字组成
        #
        curLis = [1,2]  ## 到现在为止的武器库
        heji = [0,1,2,3]  ## 初始1,2 可以构成的数
        curLis = curLis + nums.copy()
        curLis = list(set(curLis))
        for num in curLis[2:]:
            heji += [oldnum + num for oldnum in heji]
            heji = list(set(heji))


        if 1 in nums:
            memoDic[1] = True
        else:
            memoDic[1] = True
            cnt+= 1
        if 2 in nums:
            memoDic[2] = True
        else:
            memoDic[2] = True
            cnt += 1

        # for num in range(3,n+1):
        #     if num in nums:
        #         memoDic[num] = True
        #         curLis.append(num)
        #         heji += [oldnum + num for oldnum in heji]
        #         heji = list(set(heji))
        #         continue
        #
        #     ##超时，需要在 3 到 n 的遍历中 融入 dp
        #     if num in heji:
        #         print("有,cnt 不需要加",num)
        #     else:
        #         curLis.append(num) ## 更新武器库
        #         cnt += 1
        #         heji += [oldnum + num for oldnum in heji]
        #         heji = list(set(heji))
        num = 3
        step = 1
        while num <= n:
            if num in nums:
                curLis.append(num)
                heji += [oldnum+num for oldnum in heji]
                heji = list(set(heji))
                step = num
                num += step
                print(num)
                continue

            if num in heji:
                print("有,cnt 不需要加", num)
                num += 1
            else:
                curLis.append(num) ## 更新武器库
                print("没有，增加num",num)
                cnt += 1
                heji += [oldnum + num for oldnum in heji]
                heji = list(set(heji))
                step = num
                num += step
        return cnt

res  = Solution().minPatches([1,5,10],20)
print(res)

# xx = 5
#
# import  numpy as np
# lll = np.linspace(1,100,100)
# print(lll)
#
# llls = list(lll)
# print(llls)
#
# qwer = llls[20:1000:3]
# print(qwer)


