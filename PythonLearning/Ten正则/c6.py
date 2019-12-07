## 贪婪与非贪婪

import re
a = "python 1111java678php"
# python 默认使用贪婪的匹配规则，竟可能的让匹配的字符串变长.

r  = re.findall('[a-z]{3,6}',a) # {3-6} 表示匹配连续3-6个
print(r)  ## ['python', 'java', 'php']

r = re.findall('[a-z]{3,6}?',a) # 后面加一个？表示非贪婪匹配
print(r) ## ['pyt', 'hon', 'jav', 'php']

