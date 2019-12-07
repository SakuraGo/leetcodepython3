student = {
    "喜小乐":18,
    "sgd":20,
    'hxw':15
}

b = [key+str(value) for key,value in student.items()]
print(b)  # ['喜小乐18', 'sgd20', 'hxw15']

rs = {value:key for key,value in student.items()}
print(rs)  # {18: '喜小乐', 20: 'sgd', 15: 'hxw'}

b = (key for key,value in student.items())
print(b)  #<generator object <genexpr> at 0x0000025874612468>

for x in b:
    print(x)

#喜小乐
# sgd
# hxw

yuanzu = (3,5,6,7,8)
for n in yuanzu:
    print(n)