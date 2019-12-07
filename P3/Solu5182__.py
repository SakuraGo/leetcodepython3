
# 算法
# (暴力枚举) O(n)O(n)
# 设 f(i)f(i) 表示选中 ii 结尾的且没有删除过元素的最大子数组，g(i)g(i) 表示以 ii 结尾的，但删除过元素的最大子数组。
# 初始时，f(0)=a(0)f(0)=a(0)，g(0)=−∞g(0)=−∞，其余元素待定。
# 转移时，对于 f(i)f(i) 我们有两种选择，一种是用之前的结果和当前元素累加或者直接从当前元素重新开始。对于 g(i)g(i)，我们也有两种选择：不删除当前元素，即从 g(i−1)+arr(i)g(i−1)+arr(i) 转移；或者删除了当前元素，即从 f(i−1)f(i−1) 转移。
# 最终答案为 max(f(i),g(i))max(f(i),g(i))。
# 时间复杂度
# 状态数为 O(n)O(n)，每次转移仅需 O(1)O(1) 的时间，故总时间复杂度为 O(n)O(n)。
# 空间复杂度
# 需要额外 O(n)O(n) 的空间记录状态。
#
print()
'''
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int n = arr.size();
        vector<int> f(n), g(n);
        int ans = arr[0];

        f[0] = arr[0];
        g[0] = -2000000000;

        for (int i = 1; i < n; i++) {
            f[i] = max(f[i - 1] + arr[i], arr[i]);
            g[i] = max(g[i - 1] + arr[i], f[i - 1]);
            ans = max(ans, max(f[i], g[i]));
        }

        return ans;
    }
};



'''