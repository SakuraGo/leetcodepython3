##第三个参数，匹配模式参数

import re
language  = 'PythonC#JavaPHP'

r  =re.findall('c#',language)  ## 默认区分大小写，故匹配不到
print(r)  ## []

##使用第三个参数
r  =re.findall('c#',language,re.I) ## re.I 忽略大小写
print(r)

language  = 'PythonC#\nJavaPHP'
r  =re.findall('c#.{1}',language,re.I)
print(r) # []

r  =re.findall('c#.{1}',language,re.I | re.S) ## re.S 使得 . 包括换行符
print(r) # ['C#\n']

c = 'PythonPythonPythonPythonPython'

r4 = re.search('(Python){3}',c)

print(r4.group(0))

