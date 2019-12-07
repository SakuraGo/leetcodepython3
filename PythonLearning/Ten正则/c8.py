## 边界匹配
import re
qq = '11235617901'

r = re.findall('',qq)

## 是否是4~8位qq号
r = re.findall('[0-9]{4,8}',qq)
print(r)  ## ['100001']


r = re.findall('\d{4,8}',qq)
print(r)  ## ['11235566'] 超出8位会匹配前8位

r = re.findall('^\d{4,8}$',qq)  ## 边界匹配，将匹配整个qq字符串
print(r)  ## []

## ^ 从字符串开始匹配
## $ 从字符串结尾开始匹配

qq = '1000000001'
r = re.findall('000',qq)
print(r)  ## ['000', '000']

r = re.findall('^000',qq)
print(r) ## [] 若从头开始匹配 则匹配不到000，因为开头是1

r = re.findall('000$',qq)
print(r)  ## []
