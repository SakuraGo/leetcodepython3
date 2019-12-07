from enum import Enum
##枚举转换
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4
a = 1
if a == VIP.YELLOW :  #
    print("yellow")

print(type(VIP.YELLOW )) #<enum 'VIP'>

a = 1 ##由数值查询枚举名称.
print(VIP(a)) # VIP.YELLOW