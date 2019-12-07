# 5091. 建造街区的最短时间

# 你是个城市规划工作者，手里负责管辖一系列的街区。在这个街区列表中 blocks[i] = t 意味着第  i 个街区需要 t 个单位的时间来建造。
#
# 由于一个街区只能由一个工人来完成建造。
#
# 所以，一个工人要么需要再召唤一个工人（工人数增加 1）；要么建造完一个街区后回家。这两个决定都需要花费一定的时间。
#
# 一个工人再召唤一个工人所花费的时间由整数 split 给出。
#
# 注意：如果两个工人同时召唤别的工人，那么他们的行为是并行的，所以时间花费仍然是 split。
#
# 最开始的时候只有 一个 工人，请你最后输出建造完所有街区所需要的最少时间。

# 输入：blocks = [1,2], split = 5
# 输出：7
# 解释：我们用 5 个时间单位将这个工人分裂为 2 个工人，然后指派每个工人分别去建造街区，从而时间花费为 5 + max(1, 2) = 7

from typing import  List
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        startSplit = 0
        while startSplit<12:
            workers = 1
            for epoch in range(startSplit):
                workers *= 2


            startSplit+= 1
