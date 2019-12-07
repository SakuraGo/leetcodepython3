'''
public class Solution {
    public int minPatches(int[] nums, int n) {
        int patches = 0, i = 0;
        long miss = 1; // use long to avoid integer overflow error
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) // miss is covered
                miss += nums[i++];
            else { // patch miss to the array
                miss += miss;
                patches++; // increase the answer
            }
        }
        return patches;
    }
}
'''

from typing import  List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        i = 0
        miss = 1   ##表示下一个不能被表示的数
        while miss <= n:
            if (i< len(nums) and nums[i] <= miss):

                miss += nums[i]     ## 由于miss-1依旧可以被表示，而现有武器库中的尚未被使用的num[i]依旧比 miss 小，所以可以加入num[i]，这样miss就可以被表示了，于是下一个miss 就成了 miss + num[i]
                i += 1           ## 下一个未被使用的 数字序号更新
            else:
                miss += miss     ## 武器库补充上miss这个数，于是下一个miss 就成了 miss + miss
                patches += 1    ## 加了一次计数
        return patches

'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        if not nums:
            return math.floor(math.log(n, 2)) + 1
        if not n:
            return 0
        if nums[0] == 1:
            mid_max, res, i = 1, 0, 1
        else:
            mid_max, res, i = 1, 1, 0
        length = len(nums)
        while mid_max < n:
            max_add = mid_max + 1
            if i < length and nums[i] <= max_add:
                mid_max += nums[i]
                i += 1
            else:
                res += 1
                mid_max += max_add
        return res
'''

'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #当1~n-1均满足nums数组条件时，判断n是否满足的方法是：
        #若nums中所有小于等于n的项相加大于等于n时，则存在；小于n，则不存在
        #理由：nums中均为正整数，显然如果所有小于等于n的数相加仍小于n，则不存在，nums数组添加n
             #如果相加等于n，好的，满足了
             #如果所有小于等于的相加大于n,就取从小到大相加到刚好大于n，b={a1,a2......ai}就好了，这里假设结果为sum(b)=n+k好了，显然，nums中的数从小到大加到刚好大于n就停止，k<n.所以k满足nums数组条件，且必定是由b={a1,a2......ai}中的几个数相加得到，那么去掉相加为k的这几个数，b=n
        #nums数组已排好顺序，优化一下，得到一下代码
        res=1
        s=0
        i=0
        while res<=n:
            if i<len(nums) and nums[i]<=res:
                res+=nums[i]
                i+=1
            else:
                res+=res
                s+=1
        return s
'''

res = Solution().minPatches([1,3],6)