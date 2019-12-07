from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class VIP2(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1

result = VIP.GREEN == VIP.BLACK
print(result) #False
print(VIP.RED == VIP.RED) #True
print(VIP.BLACK == 3) #False
print(VIP.BLACK.value == 3) #True

#枚举类型不支持大小><比较 但可以做等值比较 ==
# print(VIP.GREEN > VIP.BLACK) #not supported between instances of 'VIP' and 'VIP'

#身份比较
print(VIP.GREEN is VIP.GREEN) #True

print(VIP.GREEN == VIP2.GREEN) #False 根本不是同一个枚举.
