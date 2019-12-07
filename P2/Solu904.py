# 904. 水果成篮  显示英文描述
#
# 题目难度 Medium
# 在一排树中，第 i 棵树产生 tree[i] 型的水果。
# 你可以从你选择的任何树开始，然后重复执行以下步骤：
#
# 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
# 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
# 请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。
#
# 你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
# 用这个程序你能收集的水果总量是多少？

from typing import  List

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree)<2:
            return len(tree)

        maxxLen = 0
        tempLen = 0
        tempCom = None  ##目前的最长组合
        num1Index = None,None ## 记录第二类节点的num,index

        for index,t in enumerate(tree):
            print(t)
            if  tempCom is None  or len(tempCom)<2:
                tempLen += 1
                maxxLen = max(maxxLen, tempLen)
                if tempCom is None:
                    tempCom = (t,)  ##这样表示一个存有唯一值 t 的元组 tempCom
                    continue
                if t not in tempCom:

                    tempCom = tempCom + (t,)
                    num1Index = t,index

                print(tempCom)
                print(num1Index)
                continue

            if t in tempCom:
                tempLen += 1
                maxxLen = max(maxxLen,tempLen)
                if t != num1Index[0]:
                    tempCom = num1Index[0] ,t
                    num1Index = t,index

            else: ##新的数出现
                tempLen = index - num1Index[1] + 1
                tempCom = tempCom[1],t
                maxxLen = max(tempLen,maxxLen)
                num1Index = t,index

        return maxxLen

# asd = 2,3
# print(asd)
# print(asd.index(3))
#
# print(len(asd))
# ew = (5)
#
# print(asd)
# abc = (1,2)
# print(abc)
# cd = (5,)
# print(abc+cd)

res = Solution().totalFruit([1,0,1,4,1,4,1,2,3])
print("res:",res)