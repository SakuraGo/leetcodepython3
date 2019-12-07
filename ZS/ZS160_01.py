# 5238. 找出给定方程的正整数解  显示英文描述
# 用户通过次数 42
# 用户尝试次数 50
# 通过次数 42
# 提交次数 52
# 题目难度 Easy
# 给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
#
# 给定函数是严格单调的，也就是说：
#
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)

# 1 <= function_id <= 9
# 1 <= z <= 100
# 题目保证 f(x, y) == z 的解处于 1 <= x, y <= 1000 的范围内。
# 在 1 <= x, y <= 1000 的前提下，题目保证 f(x, y) 是一个 32 位有符号整数。
from  typing import  List
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []

        for i in range(1,z+1):
            for j in range(1,z+1):
                if customfunction.f(i,j) == z:
                    res.append([i,j])
        return res

        # # print(customfunction)
        # if customfunction>2:
        #     return []
        # print(customfunction.f(2,3))
        # flag = True
        # if customfunction.f(2,3) == 5:
        #     flag = True
        # else:
        #     flag = False
        # # res = []
        #
        # if flag :
        #     res = [[i,z-i] for i in range(1,z)]
        #     return res
        # else:
        #     res = [[i,z//i] for i in range(1,z+1) if i * (z//i) == z]
        #     return res
        # res = []



res = Solution().findSolution(1,5)
print(res)