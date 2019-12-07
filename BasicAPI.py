## 字典删除键
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']  # 删除键是'Name'的条目
dict.clear()  # 清空字典所有条目
del dict  # 删除字典

##items() 与 dict 互相转换
memoDic = {"qwe":23,"abd":88}
items = list(memoDic.items())

memoDic = dict((items))