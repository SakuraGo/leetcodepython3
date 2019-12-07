
def add(x,y):
    return x+y
    pass

#匿名函数 lambda表达式.
lambda x,y:x+y  ##输入x，y 返回 x+y  ##
# lambda x,y:a = x+y  SyntaxError: can't assign to lambda
print(add(1,2)) #3

f = lambda x,y:x+y  ##param_list: expression

print(f(1,2)) #3

# print(f(1,2,3))
# #TypeError: <lambda>() takes 2 positional arguments but 3 were given

