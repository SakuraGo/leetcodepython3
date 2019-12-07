from typing import List
'''
我推荐的思路参考这里：https://github.com/liuyubobobo/Play-Leetcode/blob/master/1124-Longest-Well-Performing-Interval/cpp-1124/main2.cpp
简单的说，把 > 8的时间记为1，<= 8 的时间记为-1。题目就是求一个最长的区间，区间和 > 0。
可以使用二分搜索法，验证整个序列是否存在某个区间，长度 >= mid，且区间和 > 0。
具体验证的时候，使用了一个辅助数组presum。这是看区间和问题的常用套路。
presum[i] 表示 arr[0...i]的数字和，看区间[x, y]的数字和，只需要看presuum[y] - presum[x - 1]。
'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = list()
        s.append(0)
        for h in hours:
            s.append(s[-1] + (h > 8))
        # print(s)
        for i in range(len(s)):
            s[i] = s[i] * 2 - i
        print(s)
        q = list()
        q.append(0)
        ans = 0
        for i in range(1, len(s)):
            if s[i] <= s[q[-1]]:
                print('q++:%s'%i)
                q.append(i)
            else:
                l, r, choose = 0, len(q) - 1, -1
                while l <= r:
                    mid = (l + r) // 2
                    if s[i] > s[q[mid]]:
                        r = mid - 1
                        choose = mid
                    else:
                        l = mid + 1
                print("chs =", i, choose)
                ans = max(ans, i - q[choose])
            print(q, ans)
        return ans

# asdf = [1,9,9,6,10,0,6,6,9]
asdf = [9,9,9,9,9]
res = Solution().longestWPI(asdf)