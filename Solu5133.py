# 5133. 绝对值表达式的最大值  显示英文描述
#
# 给你两个长度相等的整数数组，返回下面表达式的最大值：
#
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#
# 其中下标 i，j 满足 0 <= i, j < arr1.length。

# 输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# 输出：13

from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ret = 0

        a = [0] + arr1
        b = [0] + arr2

        for ka in range(-1,3,2):
            for kb in range(-1,2,2):
                print(ka,kb)
                minn = 99999999
                for i in range(1,len(a)):

                    s = ka* a[i] + kb*b[i] + i
                    minn = min(s,minn)
                    ret = max(ret,s-minn)
                    print(s)
        print(ret)
        return ret


res= Solution().maxAbsValExpr([1],[2])


'''
class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):

        n = len(arr1)
        ret = 0
        f = [-1000000000] * 8
        for i in range(n):
            tmp = [arr1[i], arr2[i], i]
            for s in range(8):
                x = 0
                for j in range(3):
                    if (s & (1 << j)) > 0:
                        x += tmp[j]
                    else:
                        x -= tmp[j]
                if i > 0 and x + f[s ^ 7] > ret:
                    ret = x + f[s ^ 7]
                if x > f[s]:
                    f[s] = x
        return ret
'''

'''
const int MAXN = 40010;
const int INF = 1000000000;

int a[MAXN], b[MAXN], s[MAXN];

class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        for (int i = 0; i < n; ++ i)
        {
            a[i+1] = arr1[i];
            b[i+1] = arr2[i];
        }
        
        int ret = 0;
        // i > j
        /*
        a[i]-a[j]+b[i]-b[j]+i-j == (a[i]+b[i]+i) - (a[j]+b[j]+j);
        a[i]-a[j]-b[i]+b[j]+i-j == (a[i]-b[i]+i) - (a[j]-b[j]+j);
        -a[i]+a[j]+b[i]-b[j]+i-j == (-a[i]+b[i]+i) - (-a[j]+b[j]+j);
        -a[i]+a[j]-b[i]+b[j]+i-j == (-a[i]-b[i]+i) - (-a[j]-b[j]-j);
        */
        
        for (int ka = -1; ka <= 1; ka += 2)
            for (int kb = -1; kb <= 1; kb += 2)
            {
                int minv = INF;
                for (int i = 1; i <= n; ++ i)
                {
                    s[i] = ka*a[i]+kb*b[i]+i;
                    minv = min(minv, s[i]);
                    ret = max(ret, s[i]-minv);
                }
            }
        return ret;
    }
};
'''