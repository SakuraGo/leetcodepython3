# 1118. 一月有多少天
# 指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        data = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if M != 2:
            return data[M]
        else:
            if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
                return 29
            else:
                return 28



