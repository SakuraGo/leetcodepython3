import re
s = 'A8C37221D86'

##替换数字.
def convert(valueee):  ##输入与返回都得是str
    num = valueee.group()
    if int(num)>5:
        return '9'
    else:
        return '0'
    pass

r = re.sub('\d',convert,s) ## 传入了一个convert函数，自定义改变匹配到的字符串.
print(r)

def convert2(valueee):  ##输入与返回都得是str
    num = valueee.group()
    if int(num)>10:
        return '99'
    else:
        return ''
    pass

r = re.sub('\d{1,10}',convert2,s) ## 传入了一个convert函数，自定义改变匹配到的字符串.
print(r)