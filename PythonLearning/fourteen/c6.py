a = ''
b = False
c = []
print(a == None)
print(b== None)
print(c==None)


def fun():
    return None

a = fun()

if not a :#s
    print("s")
else:
    print("f")

if a is None:#s
    print("s")
else:
    print("f")

a = []
if not a :  #s 空列表判断bool值返回s  ##判空操作
    print("s")
else:
    print("f")

if a is None:#f
    print("s")
else:
    print("f")