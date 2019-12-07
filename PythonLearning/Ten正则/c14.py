import re

s = 'life is short ,i use python'
#None
r = re.search('(life.*python)',s)  # \w 就不行，有空白字符 所以用 .
print(r.group())

## 获取中间内容
print(r.group())

r = re.search('(life.*python)',s)  # \w 就不行，有空白字符 所以用 .
print(r.group(0))   # life is short ,i use python
print(r.group(1))   # life is short ,i use python

r = re.search('life(.*)py(th)on',s)  # \w 就不行，有空白字符 所以用 .
# group 记录正则表达式完整匹配结果.
# group 1 记录()内的匹配结果.
print(r.group(0))   # life is short ,i use python
print(r.group(1))   #  is short ,i use
print(r.group(2))

r = re.findall('life(.*)python',s)
print(r)  # [' is short ,i use ']

s = 'life is short ,i use python,i love python'


r = re.search('life(.*)python(.*)python',s)
print(r.group(0))  ##整体匹配字符串
print(r.group(1))  ##第一个括号
print(r.group(2))  ##第二个括号
print(r.group(0,1,2)) #返回0,1,2元组
#('life is short ,i use python,i love python', ' is short ,i use ', ',i love ')
print(r.groups()) ## 返回2个括号内的东西.
# (' is short ,i use ', ',i love ')