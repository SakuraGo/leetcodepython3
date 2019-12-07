#map 与 lambda

list_x = [1,2,3,4,5,6,7]
list_y = [1,2,3,4,5,6,7,8]

def square(x):
    return x*x

r = map(lambda x:x*x , list_x)
print(list(r))  #[1, 4, 9, 16, 25, 36, 49, 64]

r  = map(lambda x,y : x*x + y,list_x,list_y) #参数数量与 后面的列表数量要匹配.
print(list(r)) #[2, 6, 12, 20, 30, 42, 56, 72]

#list_y 少1个元素，结果是[2, 6, 12, 20, 30, 42, 56]
##返回结果个数取决于listx listy较短的那一个.