#
# 5241. 铺瓷砖  显示英文描述
# 用户通过次数 31
# 用户尝试次数 56
# 通过次数 33
# 提交次数 135
# 题目难度 Hard
# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
#
# 房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
#
# 假设正方形瓷砖的规格不限，边长都是整数。
#
# 请你帮设计师计算一下，最少需要用到多少块方形瓷砖？

class Solution:

    def __init__(self):
        self._memo = [[]]


    def gettlRecCnts(self,m,n):
        if m==0 or n==0:
            return 0
        if m == n:
            return 1
        mm, nn = max(m, n), min(m, n)

        if self._memo[mm][nn] != 0:
            print("调用memo")
            return self._memo[mm][nn]
        res = 999
        # print("m,n:",mm,nn)
        for x in range(1,nn+1):
            for y in range(0,min(x+1,nn-x+1)):
                # print("x,y = ",x,y)
                a = self.gettlRecCnts(m-x,x+y)
                b = self.gettlRecCnts(x-y,n-x)
                c= self.gettlRecCnts(m-x+y,n-x-y)
                d = self.gettlRecCnts(y,y)
                # res = min(res,(1+self.gettlRecCnts(m-x,x+y)+self.gettlRecCnts(x-y,n-x)+self.gettlRecCnts(m-x+y,n-x-y)+self.gettlRecCnts(y,y)))
                res = min(res,1+a+b+c+d)
        self._memo[mm][nn] = res
        # print("mm,nn:",mm,nn)
        return res




    def tilingRectangle(self, n: int, m: int) -> int:
        m,n = max(m,n),min(m,n)
        print("q")
        self._memo = [[0 for j in range(n+1)] for i in range(m+1)]
        # self._memo[1][2] = 3
        print("q")

        resss = self.gettlRecCnts(m,n)
        return resss

resss = Solution().tilingRectangle(11,13)
print(resss)