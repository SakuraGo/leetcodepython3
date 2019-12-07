# 5183. 一周中的第几天  显示英文描述
#
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

# 5183. 一周中的第几天  显示英文描述
#
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

class Solution:

    def isRunnian(self,year:int):
        if  year%4 == 0 and year%100 != 0 or year % 400==0:
            return True
        else:
            return False



    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ## 1971年1月1日  星期5
        mmm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        dayLis = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        daysChaju = 0

        for y in range(1971,year):
            if self.isRunnian(y):
                daysChaju+= 366
                print("366")
            else:
                daysChaju += 365
                print("365")
        for m in range(1,month):
            daysChaju += mmm[m]
            print("mmm:",m)
            if m==2 and self.isRunnian(year):
                print("runjnian")
                daysChaju+=1

        for d in range(1,day):
            print("ddd")
            daysChaju += 1

        return dayLis[(daysChaju%7+5)%7]

# res = Solution().dayOfTheWeek(1,1,1972)
# print(res)

res =Solution().isRunnian(1971)
print(res)