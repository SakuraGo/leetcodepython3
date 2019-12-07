# 5198. 丑数 III  显示英文描述  我的提交返回竞赛
#
# 请你帮忙设计一个程序，用来找出第 n 个丑数。
#
# 丑数是可以被 a 或 b 或 c 整除的正整数。

# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcd(x, y):
            if y == 0:
                return x
            else:
                return lcd(y, x % y)

        ab = a*b / lcd(a,b)
        bc = b*c / lcd(b,c)
        ac = a*c / lcd(a,c)
        abc = ab*c / lcd(ab,c)

        def curX(x):
            return x//a + x // b + x//c - x//ab - x//ac -x//bc + x // abc


        l,r = 0 ,2000000000
        while l<r:
            mid = (l+r)//2
            cnt = curX(mid)
            print(cnt)
            if cnt == n:  ##找到而不马上返回，因为49，50的curX 都是7个。。所以。。。需要继续逼近
                r = mid
            elif cnt<n:
                l = mid+1
            elif cnt>n:
                r = mid-1
        return r
res = Solution().nthUglyNumber(7,7,7,7)
print(res)
'''
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcd(x,y):
            if y==0:
                return x
            return lcd(y,x%y)
        
        ab = a * b // lcd(a,b)
        ac = a * c // lcd(a,c)
        bc = b * c // lcd(b,c)
        
        abc = ab * c // lcd(ab,c)
                
        print(ab,ac,bc,abc)
        def getDivNum(x): # [0,x]中整除的数的个数
            return x//a + x//b + x//c - x//ab - x//ac - x//bc + x//abc
        
        l,r = 0, 2000000000
        while l<r:
            mid = (l+r)//2
            num = getDivNum(mid)
            if num==n:
                r = mid
            elif num<n:
                l = mid +1
            else:
                r = mid -1
        return l

'''