# 5089. 会议日程安排  显示英文描述  我的提交返回竞赛
# 给你两位客户的可用时间间隔 slots1 和 slots2，以及会议的预计持续时间 duration，请你帮他们安排合适的会议时间。
#
# 「会议时间」是指用户都能够参加且持续时间满足预计时间 duration 的 最早的时间间隔 。
#
# 如果没有满足要求的会面时间，就返回一个 空数组 。
#
# 「时间间隔」的格式是 [start, end]，由两个元素 start 和 end 组成，表示从 start 开始，到 end 结束。
#
# 题目保证同一个人的可用时间间隔不会出现交叠的情况，也就是说，对于同一个人的两个时间间隔 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

# 输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# 输出：[60,68]

from  typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # memo1 = [0 for i in range(slots1[-1][-1]+1)]
        # memo2

        slots1 = sorted(slots1,key= lambda x:x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        res = []
        time1 = slots1.pop(0)
        time2 = slots2.pop(0)
        start1,end1 = time1
        start2,end2 = time2
        flag = True ##控制删那一个slot..
        if end1<end2:
            flag = True
        else:
            flag = False

        while len(slots1)>=0 and len(slots2)>=0:
            print("1:",start1,end1,"  2:",start2,end2)

            maxStart = max(start1,start2)
            minEnd = min(end1,end2)
            if minEnd-maxStart>= duration:
                return [maxStart,maxStart+duration]
            else:
                if flag is True and len(slots1)>0:
                    time1 = slots1.pop(0)
                    start1, end1 = time1
                    if end1 < end2:
                        flag = True
                    else:
                        flag = False
                elif flag is False and len(slots2)>0:
                    time2 = slots2.pop(0)
                    start2, end2 = time2
                    if end1 < end2:
                        flag = True
                    else:
                        flag = False
                else:
                    return []

        return res

res = Solution().minAvailableDuration([[10,50],[60,120],[140,210]],[[0,15],[60,70]],12)
print(res)