# map()
# reduce()
# filter()

list_x = [1,0,1,0,0,1]
list_u = ["a","B","c","F","e"]

#filter中的lambda表达式必须是返回真或者假的东西..
r = filter(lambda x:True if x==1 else False,list_x)

#filter和map得到的结果都是一个集合 reduce得到一个数值
print(r) #<filter object at 0x000001ABA0C79240>

print(list(r)) #[1,1,1]

r = filter(lambda x:x,list_x)
print(list(r)) #[1,1,1]

#判断是否大写.
r  = filter(lambda x:True if x.isupper() else False,list_u)
print(list(r)) #['B', 'F']