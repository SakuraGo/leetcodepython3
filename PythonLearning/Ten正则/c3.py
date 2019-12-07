import re
print("zzzzzz")
s  = 'abc,acc,adc,aec,afc,ahc'
r = re.findall('acc',s)
print(r)

r = re.findall('a[cfd]c',s)  ##[]中的cf表示 匹配字符集
print(r)

r = re.findall('a[^cfd]c',s)  ##不是cfd的
print(r)

r = re.findall('a[c-f]c',s)  ## 从c到f
print(r)
