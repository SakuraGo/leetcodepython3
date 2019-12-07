# 'str'
## json字符串到python数据结构
## 这个过程也称为反序列化
import json

json_str = '{"name":"qiyue","age":18}'

student = json.loads(json_str)
print(type(student))
print(student)
print(student['name'])
print(student["age"])

json_str = '[{"name":"qiyue","age":18,"flag":false},{"name":"bayue","age":18}]'
student = json.loads(json_str)
print(type(student))
print(student)

print(student[1])
