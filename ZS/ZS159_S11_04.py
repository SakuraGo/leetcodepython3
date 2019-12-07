# 5111. 分享巧克力  显示英文描述  我的提交返回竞赛
# 用户通过次数 64
# 用户尝试次数 80
# 通过次数 66
# 提交次数 127
# 题目难度 Hard
# 你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。
#
# 你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。
#
# 为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。
#
# 请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。

# 输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
# 输出：6
# 解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。

from  typing import List
class Solution:
    def __init__(self):
        self._cakes = []
        self._k = 0
        self._res = 0

    def judge(self,mid):
        print("mid:",mid)
        cnt = 0
        curSum = 0
        for cake in self._cakes:
            curSum += cake
            if curSum>= mid:
                cnt+= 1
                curSum = 0

        return cnt>= self._k+1



    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        ##二分法查找......
        self._cakes = sweetness
        self._k = K
        right = sum(sweetness) // (K+1)
        left = 1
        while left<=right:
            mid = (left+right) // 2
            flag = self.judge(mid)
            if flag: ##可以，那么需要增加..
                self._res = max(self._res,mid)
                left = mid+1
            else:
                ##mid太大了需要减小..
                right = mid-1   ##这样处理就可以 ,left = mid 就不行..

        return self._res

res = Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9],5)
print(res)






'''


'''