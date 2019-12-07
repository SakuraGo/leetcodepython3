a,b,c = 1,2,3
d = 1,2,3
a,b,c = d
q,w,e = [1,2,3]
print(q,w,e)
print(type(q))
print(type(d))

z=1
x=1
c = 1
print(id(z),id(x),id(c)) ## 1749904416 1749904416 1749904416

f=g=h=1
print("fgh:",f,g,h)