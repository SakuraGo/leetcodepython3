# 5096. 数组变换  显示英文描述  我的提交返回竞赛
# 用户通过次数 83
# 用户尝试次数 129
# 通过次数 83
# 提交次数 166
# 题目难度 Easy
# 首先，给你一个初始数组 arr。然后，每天你都要根据前一天的数组生成一个新的数组。
#
# 第 i 天所生成的数组，是由你对第 i-1 天的数组进行如下操作所得的：
#
# 假如一个元素小于它的左右邻居，那么该元素自增 1。
# 假如一个元素大于它的左右邻居，那么该元素自减 1。
# 首、尾元素 永不 改变。
# 过些时日，你会发现数组将会不再发生变化，请返回最终所得到的数组。

from typing import List
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        flag = True
        lis = arr.copy()
        if len(arr)<3:
            return arr
        while 1:
            flag = True
            lis = arr.copy()
            for idx,num in enumerate(arr):
                if idx== 0 or idx == len(arr)-1:
                    continue
                if num< lis[idx-1] and num <lis[idx+1]:
                    arr[idx]+=1
                    flag = False
                    continue
                if num > lis[idx-1] and num>lis[idx+1]:
                    arr[idx]-=1
                    flag = False
                    continue
            if flag is True:
                return arr

        return arr


