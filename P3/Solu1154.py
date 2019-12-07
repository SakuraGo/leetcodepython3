# 1154. 一年中的第几天
# 给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
#
# 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。

# 输入：date = "2019-01-09"
# 输出：9



class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day = date.split('-')
        year = int(year)
        lis_runnian = [31,29,31,30,31,30,31,31,30,31,30,31]
        lis_pingnian = lis_runnian.copy()
        lis_pingnian[1] = 28

        lis = lis_pingnian
        if year%400 == 0 or year%4 == 0 and year%100 !=0 :
            print('runnian')
            lis = lis_runnian

        index = 0

        for mon in range(int(month)):
            if mon-1>=0:
                index += lis[mon-1]

        index += int(day)
        return index





year = 1900
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(1)