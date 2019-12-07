## 正则替换
import re

language = 'PythonC#JavaPHP'
r = re.sub('C#','GO',language,0)  ## 0表示 匹配会无限的替换下去,不限制次数
print(r)  ## PythonGOJavaPHP

language = 'PythonC#JavaPHPC#C#C#C#C#'
r = re.sub('C#','GO',language,2)  ## 0表示 匹配会无限的替换下去,不限制次数
print(r)  ## PythonGOJavaPHPGOC#C#C#C#  只换了2次

## 内置函数的替换 "str".replace
newl = language.replace('C#','GO')  ##字符串是不可变的，需要新生成一个字符串来接收
print(newl)


def convert(value): ## 被匹配到的 'C#' 会被传入到这个函数中
    print(value)
    matched = value.group()
    return " !!"+matched+"!! "
    return '5'
    ##返回的结果会是新的替换字符串

#被匹配到的 'C#' 会被传入到这个函数中
r = re.sub("C#",convert,language)
print(r) ## PythonJavaPHP 消失了.

