
##枚举与普通类的优势

yellow = 1
green = 2

{"yellow":1,"green":2}
class TypeDiamond():
    yellow = 1
    green = 2

## 可变
## 没有放置相同值的功能

class Common():
    YELLOW = 1

from enum import  Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2 ##这里弱重复定义YELLOW 会报错：YELLOW = 2 Attempted to reuse key: 'YELLOW'
    BLACK = 3
    RED = 4

Common.YELLOW = 6

print(VIP.YELLOW)
# VIP.YELLOW = 6  ## 不可更改  Cannot reassign members.