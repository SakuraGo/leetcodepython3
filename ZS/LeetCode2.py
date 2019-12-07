from typing import List
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        cur = cont[-1]
        if len(cont) == 1:
            return [cur,1]

        def zuixiaogongyueshu(x,y):
            if y == 0:
                return x
            else:
                return zuixiaogongyueshu(y,x%y)



        def qudaojiayi(a0,ress):
            print("a0:",a0)
            res0 = ress[0]
            res1 = ress[1]
            fenzi = a0*res0+res1
            fenmu = res0
            zxgys = zuixiaogongyueshu(fenzi,fenmu)
            fenzi = fenzi // zxgys
            fenmu = fenmu // zxgys
            print("fzfm:",fenzi,fenmu)
            return [int(fenzi),int(fenmu)]


        res = qudaojiayi(cont[-2],[cont[-1],1])
        # print("第一次:",res)
        for i in range(len(cont)-3,-1,-1):
            print("i:",i," res:",res)
            res = qudaojiayi(cont[i],res)

        return res

res = Solution().fraction([3, 2, 0, 2])

print(res)


'''
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        a, b = 1, cont[-1]
        for x in cont[:-1][::-1]:
            a, b = b, a + b * x
            g = math.gcd(a, b)
            a //= g
            b //= g
        return [b, a]
'''

