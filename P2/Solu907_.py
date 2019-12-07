print("qwer")

'''
思路：

考虑从A中的每个元素A[i]，如果求出包含A[i]并以A[i]为最小元素的所有子数组个数n[i]，则元素A[i]对答案ans的贡献为n[i]*A[i]，
那么我们可以先求包含A[i]并以A[i]为最小元素的最长子数组，如果A[i]左边第一个小于A[i]的元素为A[left]，
A[i]右边第一个小于A[i]的元素为A[right]，则包含A[i]并以A[i]为最小元素的最长子数组为A[left+1:right]，
满足以A[i]为最小元素的所有子数组个数n[i] = (i-left)*(right-i)。
我们用left[i]表示A[i]左边第一个小于A[i]元素的位置，用right[i]表示A[i]右边第一个小于A[i]元素的位置，left数组初始值为-1，right数组初始值为len(A)，
求解left和right可以用单调栈来实现，可以两遍遍历，也可以一遍遍历，更优化的写法还可以一边遍历一边求解ans。

时间复杂度O(N)O(N)

空间复杂度O(N)O(N)

'''

class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        if len_A == 0:
            return 0
        if len_A == 1:
            return A[0]

        ans = 0
        left = [0] * len_A
        right = [0] * len_A

        stack = []
        for i in range(len_A):
            while stack and A[stack[-1]] > A[i]:  ## 注意这里是while ，如果stack最后一个最小值的标记index 一直比A【i】 大，会一直被pop掉
                stack.pop()
            if not stack:
                left[i] = -1            ## 当前最小节点，left = -1
            else:
                left[i] = stack[-1]   ## 找到比自己小的节点的index
            stack.append(i)
            print(stack)

        stack = []
        for i in range(len_A - 1, -1, -1):
            ##我这里是假设了每个子数组如果最小值出现多次，那么只取第一次出现的最小值。所以左边取小于，右边取小于等于。
            # 其实反过来也可以。举个例子验算一下，比如原数组是[1, 1, 1]，
            # 那么对于第一个1，满足条件的子数组为，[1]，[1, 1]，[1, 1, 1]，
            # 对于第二个1，满足条件的子数组为，[1]，[1, 1]，对于第三个1，满足条件的子数组为[1]，最后结果是6。
            # 如果左右都取严格小于，那么得出的子数组只有[1]，[1]，[1]，结果是3，就不对了。
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                right[i] = len_A
            else:
                right[i] = stack[-1]
            stack.append(i)

        print(left)
        print(right)
        for i in range(len_A):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 1000000007
        return ans

res = Solution().sumSubarrayMins([1,1,1,1])
print(res)

'''
一遍遍历
class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)

作者：smoon1989
链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''