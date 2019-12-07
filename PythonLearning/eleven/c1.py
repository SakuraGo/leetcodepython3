from enum import  Enum
#python中枚举是一个类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

vvv  = VIP(3)
print(vvv.GREEN) ##VIP.GREEN  ##打印出名字而非没有意义的数字.
print(VIP.GREEN) ##VIP.GREEN