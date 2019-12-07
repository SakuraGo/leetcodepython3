import re
a = "C0C++Java7Python389jasrio6php88"

r = re.findall("\d",a) ##搜索数字
rr = re.findall("\D",a) ##搜索非数字
print(r)
print(rr)

## "Python" 普通字符
## "\d" 元字符

