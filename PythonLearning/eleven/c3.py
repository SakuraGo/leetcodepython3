from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1
asd = VIP(2)  ## VIP.GREEN
print(VIP.GREEN)       ## VIP.GREEN
print(VIP.GREEN.name)  ## GREEN
print(type(VIP.GREEN))  ## <enum 'VIP'> #一个枚举类型
print(type(VIP.GREEN.name))  ## <class 'str'>  ## 字符串
print(VIP['GREEN'])  ## 通过枚举名称获得枚举类型.. VIP.GREEN

print(VIP.GREEN.value) ## 获取后面的数值
asggg= VIP['RED']   ##获得枚举类型RED的2个办法 VIP['RED'] 或者VIP(4)
print(asggg)  #VIP.RED

#遍历枚举
for v in VIP:
    print(v)
# VIP.YELLOW
# VIP.GREEN
# VIP.BLACK
# VIP.RED