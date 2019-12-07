##列表推导式
a  = [1,2,3,4,5,5,6,7]
b = [i**2 for i in a]
print(b)

c = [i**3 for i in a]
print(c)

d = [i**2 for i in a if i >= 5]
print(d)

##set dict 元组 也可以被推导.

a = {1,2,3,4,5,6,7,8}
b = {i**2 for i in a if i>=5}
print(b)

dd = {1:2,2:3,3:4}
b = [key*value for key,value in dd.items()]
print(b)