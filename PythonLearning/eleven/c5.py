from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 1  #不同的枚举的值可以相等
    YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

for  v  in VIP:
    print(v)
# 只会打印每个数值的第一个枚举
# VIP.YELLOW    #GREEN  YELLOW_ALIAS 被视为别名没有被打印
# VIP.BLACK
# VIP.RED

for v in VIP.__members__.items():
    print(v)
# ('YELLOW', <VIP.YELLOW: 1>)
# ('GREEN', <VIP.YELLOW: 1>)
# ('YELLOW_ALIAS', <VIP.YELLOW: 1>)
# ('BLACK', <VIP.BLACK: 3>)
# ('RED', <VIP.RED: 4>)

print(VIP.__members__)

for v in VIP.__members__:  #这样只打印枚举名.
    print(v)
    # YELLOW
    # GREEN
    # YELLOW_ALIAS
    # BLACK
    # RED