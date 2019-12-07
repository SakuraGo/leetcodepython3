# 1090. 受标签影响的最大值  显示英文描述
#
# 题目难度 Medium
# 我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。
#
# 我们从这些项中选出一个子集 S，这样一来：
#
# |S| <= num_wanted
# 对于任意的标签 L，子集 S 中标签为 L 的项的数目总满足 <= use_limit。
# 返回子集 S 的最大可能的 和。
from typing import List

'''
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ## 可行 、但是超时##
        data = {}
        for i in range(len(values)):
            lab = labels[i]
            num = values[i]
            if lab in data.keys():
                data[lab] .append(num)
            else:
                data[lab] = [num,-1]

        for key in data.keys():
            lis = data[key]
            lis.sort(reverse=True)

        limit_Dic = {}
        for lab in data.keys():
            limit_Dic[lab] = use_limit

        res = 0
        for i in range(num_wanted):
            curMax = -1
            curLab = -1
            if len(data.keys()) == 0:
                print("asdf")
                break
            if len(limit_Dic.keys()) == 0:
                print("tttt")
                break

            for lab in data.keys():
                num = data[lab][0]
                if num>curMax:
                    curMax = num

                    curLab = lab

            if curMax == -1:
                break
            res += curMax
            print(curMax)
            data[curLab].pop(0)
            limit_Dic[curLab] -= 1
            if limit_Dic[curLab] <= 0:
                print("dell  "+str(curLab))
                del data[curLab]
                del limit_Dic[curLab]

        return  res
'''
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        listtt = zip(values,labels)
        listtt = sorted(listtt,reverse=True)
        limit_cnt = {}
        res = 0
        num_cnt = 0
        for num,lab in listtt:
            if lab not in limit_cnt.keys():
                limit_cnt[lab] = 0
            if limit_cnt[lab]>= use_limit:
                continue
            limit_cnt[lab]+= 1
            res += num
            num_cnt+= 1
            if num_cnt>= num_wanted:
                break
        return res






a1 = [4,9,1,1,2]
b1 = [2,2,1,2,2]
4
2
#aaas =  Solution().largestValsFromLabels([4,9,1,1,2],[2,2,1,2,2],4,2)
# print(aaas)
for i,j in zip(a1,b1):
    print(i)
    print(j)
