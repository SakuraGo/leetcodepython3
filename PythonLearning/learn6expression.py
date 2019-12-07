##算术运算符的优先级问题
a = 1
b = 2
c = 3
print(a or b and c)  ## and 优先级大于 or
print((a or b) and c)

##同级的话 ，从左到右
c = 2
print(not a  or b + 2 == c)

print((not a)  or ((b + 2) == c))

if a or  b+2 == c:
    print ("qwer")

user_account= input()  ## 让用户输入 并赋值给user_account
print(user_account)

if True:
    pass ##空语句、占位语句


