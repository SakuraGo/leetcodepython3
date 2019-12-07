import re
s = 'life is short ,i use python,i love python'
print(re.findall('(life(.*)python){1}?',s))

print(re.findall('(.*)(python)',s))