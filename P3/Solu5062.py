# 5062. 连接棒材的最低费用
# 为了装修新房，你需要加工一些长度为正整数的棒材 sticks。
#
# 如果要将长度分别为 X 和 Y 的两根棒材连接在一起，你需要支付 X + Y 的费用。 由于施工需要，你必须将所有棒材连接成一根。
#
# 返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。

## 超时 ！！！ ##
from  typing import List
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        sticks = sorted(sticks)

        while len(sticks) > 1:
            newStick = sticks[0] + sticks[1]
            res += newStick
            sticks[1] = newStick
            sticks.pop(0)
            l = 1
            r = len(sticks) - 1
            if sticks[0]> sticks[-1] and len(sticks)> 1:
                sticks = sticks[1:] + sticks[0:1]
                continue
            elif len(sticks) == 1:
                break

            # if len(sticks)<2 or sticks[0] <= sticks[1]:
            #     continue
            while l < r:
                mid = (l+r) // 2
                if sticks[mid]> sticks[0]:
                    r = mid
                elif sticks[mid] == sticks[0]:
                    l = r = mid
                    break
                elif sticks[mid] < sticks[0]:
                    if l == mid:
                        break
                    else:
                       l = mid

            sticks = sticks[1:r]+sticks[0:1] + sticks[r:]
            print(sticks)
        return res

res = Solution().connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009])
print(res)