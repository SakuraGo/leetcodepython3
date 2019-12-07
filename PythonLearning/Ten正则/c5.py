#数量词
import re
a = "python 111java678php"
r = re.findall('[a-z][a-z][a-z]',a) ##匹配连续3个字母
print(r)  ## ['pyt', 'hon', 'jav', 'php']

r  = re.findall('[a-z]{3}',a) # {3} 表示匹配3个
print(r)  ## ['pyt', 'hon', 'jav', 'php']

r  = re.findall('[a-z]{3,6}',a) # {3-6} 表示匹配连续3-6个
print(r)  ## ['python', 'java', 'php']

asdg = 'PythonnnPythonPythonPythonPython'
r = re.findall('Python{3}',asdg)
print(r)  ## ['Pythonnn']