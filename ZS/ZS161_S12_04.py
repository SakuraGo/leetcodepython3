# 5115. 删除回文子数组  显示英文描述  我的提交返回竞赛
# 用户通过次数 20
# 用户尝试次数 37
# 通过次数 22
# 提交次数 62
# 题目难度 Hard
# 给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
#
# 注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。
#
# 请你计算并返回从数组中删除所有数字所需的最少操作次数。

# 输入：arr = [1,2]
# 输出：2
# 示例 2：
#
# 输入：arr = [1,3,4,1,5]
# 输出：3
# 解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
from  typing import List
class Solution:
    ##python3 超时
    def minimumMoves(self, arr: List[int]) -> int:
        lenn = len(arr)
        dp = [[999 for m in range(lenn)] for n in range(lenn)]
        ##init
        for ii in range(len(dp)):
            dp[ii][ii] = 1
            if ii<lenn-1:
                dp[ii][ii+1] = 1 if arr[ii] == arr[ii+1] else 2

        print(dp)

        for k in range(2,lenn):
            for i in range(0,lenn-k):
                j = i+k
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    ##从两边搞东西..
                    # minnn = min(dp[i][j-1]+1,dp[i+1][j]+1)
                    # ##
                    # dp[i][j] = min(minnn,dp[i+1][j-1]+2)
                    ##此处采用区间DP
                    # dp[i][j] = (把这段i-j 分成两段,结果为两段的和)
                    for mid in range(i,j):
                        dp[i][j] = min(dp[i][j],dp[i][mid]+dp[mid+1][j])



        print("dp:",dp)
        return dp[0][-1]

res = Solution().minimumMoves([2,20,12,6,13,16,16,18,11,15,14,13,10,8,17,14,10,9,11,14,11,20,20,13,8,5,7,3,2,2,20,12,8,7,16,6,1,16,9,3,2,16,19,14,15,2,19,10,18,13,11,20,5,5,19,11,3,1,15,14,16,10,10,2,20,13,15,20,11,10,4,5,1,15,6,9,11,16,13,17,2,5,12,20,5,14,10,15,20,7,11,17,18,10,5,14,12,11,10,20])
print(res)


























'''
//混合dp
//dp[i][j] 删掉它们用的最小次数

//dp[i][j]等于多个内部分两块然后切开
//如果arr[i] == arr[j] 那么 dp[i][j] = min(dp[i - 1][j - 1], dp[i][j])

//初始化dp[i][i] = 1
// dp[i][i + 1] = 2 如果arr[i] != arr[i + 1] 否则 1

class Solution {
public:
	int minimumMoves(vector<int>& arr) {
		int aSize = arr.size();
		vector<vector<int>> dp(aSize, vector<int>(aSize, INT_MAX));

		for (int i = 0; i < aSize; ++i)
			dp[i][i] = 1;

		for (int i = 0; i < aSize - 1; ++i)
		{
			if (arr[i] == arr[i + 1]) dp[i][i + 1] = 1;
			else dp[i][i + 1] = 2;
		}

		for (int len = 3; len <= aSize; ++len)
		{
			for (int left = 0; left <= aSize - len; ++left)
			{
				int right = left + len - 1;
				for (int mid = left; mid < right; ++mid)
				{
					dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid + 1][right]);
				}
				if (arr[left] == arr[right])
					dp[left][right] = min(dp[left][right], dp[left + 1][right - 1]);
			}
		}
		return dp[0][aSize - 1];
	}
};
'''