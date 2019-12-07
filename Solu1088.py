# 1088. 易混淆数 II  显示英文描述
# 用户通过次数 16
# 用户尝试次数 57
# 通过次数 16
# 提交次数 153
# 题目难度 Hard
# 本题我们会将数字旋转 180° 来生成一个新的数字。
#
# 比如 0、1、6、8、9 旋转 180° 以后，我们得到的新数字分别为 0、1、9、8、6。
#
# 2、3、4、5、7 旋转 180° 后，是 无法 得到任何数字的。
#
# 易混淆数（Confusing Number）指的是一个数字在整体旋转 180° 以后，能够得到一个和原来 不同 的数，
# 且新数字的每一位都应该是有效的。（请注意，旋转后得到的新数字可能大于原数字）
#
# 给出正整数 N，请你返回 1 到 N 之间易混淆数字的数量。
# class Solution {
# private:
#     int
#
#
# cnt = 0;
# unordered_map < int, int > m;
#
# public:
#
# void
# dfs(int
# i, int
# n, long
# long
# curr, long
# long
# curr2) {
# if (curr2 > n)
# {
# return;
# }
# if (curr != curr2) {
# ++cnt;
# }
# for (auto x: m) {
#     if (curr == 0 & & x.first == 0) {
#     continue;
#     }
#     long
#     long
#     nextCurr2 = 10 * curr2 + x.first;
#     long
#     long
#     nextCurr = pow(10, i) * x.second + curr;
#     dfs(i + 1, n, nextCurr, nextCurr2);
#     }
#     }
#
#     int
#     confusingNumberII(int
#     N) {
#         m[0] = 0;
#     m[1] = 1;
#     m[6] = 9;
#     m[8] = 8;
#     m[9] = 6;
#     dfs(0, N, 0, 0);
# return cnt;
# }
# };
