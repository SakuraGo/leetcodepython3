from enum import Enum
from enum import IntEnum,unique

@unique  ##不允许相同的枚举值
# BLUE = 1 会报错
class VIP(IntEnum):  ## IntEnum 中每个数值必须是 int
    YELLOW = 1
    BLUE = 1  ## duplicate values found in <enum 'VIP'>: BLUE -> YELLOW
    # GREEN = 'qw' #ValueError: invalid literal for int() with base 10: 'qw'
    BLACK = 3
    RED = 4

## 枚举类型没有实例化的。。单例模式.
