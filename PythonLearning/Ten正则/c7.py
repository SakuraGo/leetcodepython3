## 数量词
# * 匹配*前面的字符0次或者无线多次
# +匹配一次或者无限多次
# ?匹配0次或者1次

import re
a = 'pytho0python1pythonn2'

r = re.findall('python*',a)
print(r) ## ['pytho', 'python', 'pythonn']

r = re.findall('python+',a)
print(r) ## ['pytho', 'python', 'pythonn']

r = re.findall('python?',a)
print(r) ## ['pytho', 'python', 'python']  ##可用于去重..

## 上一章中{3,6}? 的问号出现在一个范围之后，表示非贪婪
## 这章的 ?直接出现在字符之后 ，表示 匹配0或1次.


r = re.findall('python{1,2}',a)
print(r) ## ['python', 'pythonn']

r = re.findall('python{1,2}?',a)
print(r) ## ['python', 'python']