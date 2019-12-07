import re  ## match 和 search
s = 'A83C72D1D8E67'

r = re.match('\d',s)  ## 从s的开头开始匹配
print(r)   #None

r1 =re.search("\d",s)  ## 搜索整个s，一旦找到第一个匹配就返回.
print(r1) ## <_sre.SRE_Match object; span=(1, 2), match='8'>

print()

s = '83C72D1D8E67'
r = re.match('\d',s)  ## 从s的开头开始匹配
print(r)   #<_sre.SRE_Match object; span=(0, 1), match='8'>
print(r.span()) #(0,1)

r1 = re.search("\d",s)
print(r1.group())  ## group()返回结果.

r2 = re.findall('\d',s)
print(r2)