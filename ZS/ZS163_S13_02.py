# 5109. 最小公共区域  显示英文描述  我的提交返回竞赛
# 用户通过次数 40
# 用户尝试次数 60
# 通过次数 40
# 提交次数 80
# 题目难度 Medium
# 给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。
#
# 很自然地，如果区域 X 包含区域 Y ，那么区域 X  比区域 Y 大。
#
# 给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。
#
# 如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。
#
# 数据同样保证最小公共区域一定存在。
from typing import  List
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        ##思路是改造一个树。。


        return 1

# ###
## 阿坑哥的思路是也是搞一个树，
# 然后用一个先从region1开始向上找父亲
# 一路沿途的所有节点都被标记为true
# 再从region2开始往上找，碰到第一个被标记过的就是第一个包含这两个region的节点
#         class Solution {
#         public:
#             map < string, string > fa;
#             map < string, bool > vis;
#             string
#
#         findSmallestRegion(vector < vector < string >> & regions, string
#         region1, string
#         region2) {
#             fa.clear();
#         vis.clear();
#
#         for (auto & v: regions)
#         for (int i = 1, len = v.size(); i < len; ++i)
#         fa[v[i]] = v[0];
#
#         do{
#         vis[region1] = true;
#         if (fa.count(region1) == 0)
#         break;
#         region1 = fa[region1];
#
#     }while (true);
#
#     do
#     {
#     if (vis[region2])
#     return region2;
#     region2 = fa[region2];
#
# }while (true);
# }
# };
