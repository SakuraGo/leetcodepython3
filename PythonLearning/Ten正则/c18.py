## 序列化

# json   Python
# object dict
# array  list
# string str
# number int
# number float
# true   True
# false  False
# null   None

import json
student = [{'name': 'qiyue', 'age': 18, 'flag': False},
           {'name': 'bayue', 'age': 18}]

jstr = json.dumps(student)
print(jstr)
