## 概括字符集

import re

a = 'python1 1G\nZA\r&_@1j……ava6+8pp'

r = re.findall('\d',a)
## eg: \d ,概括了所有的数字
## \D 所有非数字

print(r)
r = re.findall('\D',a)
print(r)
r = re.findall('[0-9]',a)
print(r)
r = re.findall('[^0-9]',a)
print(r)

## \w  数字和字母,单词字符  [A-Za-z0-9]
r = re.findall('\w',a)
print(r)
r = re.findall('[A-Za-z0-9_]',a)
print(r)  ## ['p', 'y', 't', 'h', 'o', 'n', '1', '1', 'G', 'Z', 'A', '_', '1', 'j', 'a', 'v', 'a', '6', '8', 'p', 'p']
##概括字符集或者是字符集都只能匹配单一的字符

r = re.findall('\W',a) #非单词字符
print(r) ## [' ', '\n', '\r', '&', '@', '…', '…', '+']

r = re.findall('\s',a) ##空白字符
print(r) ## [' ', '\n', '\r']

r = re.findall('\S',a) ##非空白字符
print(r) ## ['p', 'y', 't', 'h', 'o', 'n', '1', '1', 'G', 'Z', 'A', '&', '_', '@', '1', 'j', '…', '…', 'a', 'v', 'a', '6', '+', '8', 'p', 'p']

## . 匹配出了换行符\n之外的所有字符
