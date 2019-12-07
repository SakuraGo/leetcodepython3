## 正则表达式

'''
正则表达式是一个特殊的字符串
一个字符串是否与我们所设定的字符序列相匹配
快速检索文本，实现一些替换文本的操作
'''

# eg:检查一串数字是否是电话号码
# 监测一个字符串是否符合email
# 把文本里指定的单词替换为另外一个单词

a  = "C|C++|Java|C#|Python|Javascript"
# print("Python" in a)
# print(a.index("Pythono")>-1)
import re

# re.findall("正则表达式","被检查的字符串")
r = re.findall("Python",a)
if len(r)!= 0:
    print("字符串中包含Python ")
else:
    print("No")
print(r)  ## ['Python']
