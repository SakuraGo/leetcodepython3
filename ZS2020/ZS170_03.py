# 5305. 获取你好友已观看的视频  显示英文描述  我的提交返回竞赛
# # 用户通过次数 0
# # 用户尝试次数 0
# # 通过次数 0
# # 提交次数 0
# # 题目难度 Medium
# # 有 n 个人，每个人都有一个  0 到 n-1 的唯一 id 。给你数组 watchedVideos  和 friends ，其中 watchedVideos[i]  和 friends[i] 分别表示 id = i 的人观看过的视频列表和他的好友列表。
# #
# # Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 k 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。
# #
# # 给定你的 id  和 level ，请你返回所有指定 level 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按名字字典序从小到大排列。

# 输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
# 输出：["B","C"]
# 解释：
# 你的 id 为 0 ，你的朋友包括：
# id 为 1 -> watchedVideos = ["C"]
# id 为 2 -> watchedVideos = ["B","C"]
# 你朋友观看过视频的频率为：
# B -> 1
# C -> 2

from  typing import  List
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = [id]
        # watchedVideos[id] = []
        lev = 0
        upper = [id]
        down = []
        while lev < level:
            down = []
            for pid in upper:
                fri = friends[pid]
                for p in fri:
                    if p not in visited:
                        down.append(p)
                        visited.append(p)
                        # watchedVideos[p] = []

            upper = down.copy()
            lev+= 1

        finalLis = []
        for idx in down:
            finalLis += watchedVideos[idx]



        print(finalLis)
        finalLis.sort(reverse=True)
        cntDic = {}
        for tv in finalLis:
            if tv in cntDic:
                cntDic[tv]+= 1
            else:
                cntDic[tv] = 1
        diclis = list(cntDic.items())
        print(diclis)
        diclis.sort(key=lambda x:x[1],reverse=False)
        print(diclis)
        return [item for item,cnt in diclis]


res  = Solution().watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]],[[1,2],[0,3],[0,3],[1,2]],0,1)
print(res)








