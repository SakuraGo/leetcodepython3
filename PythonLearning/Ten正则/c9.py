import re

## 这一节课有点问题？？？

a  = 'PythonPythonPythonPythonPythonPython'

#target Python重复多次的情况

r = re.findall('PythonPythonPython',a)
print(r) ## ['PythonPythonPython', 'PythonPythonPython']

r = re.findall('Python{3}',a)  ##单个字符重复
print(r) ## []

## (  ) 表示 一个组 {3} 依然是重复次数 数量词
r = re.findall('(Python){2,3}',a)
print(r) ##['Python', 'Python']

# [abc] 或a或b或c
# (abc) 表示且关系