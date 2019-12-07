print(type(1))
print(type(-1))
print(type(1.1))
print(type(1.111111))
print(type(1+1.0))
print(type(1*1.0))
print()
print(type(2/2))    ## 得到float  1.0
print(type(2//2))  ##得到整形 int 1
print(0b10)  ## 2进制
print(0b11)
print(11)
print(0o10)  ## 8进制
print(0o11)  ##
print(0x10)  ## 16进制
print(0x1F)
print(bin(11))  ## 0b1011 bin:转二进制
print(bin(0xE)) ## 0b1110
print(int(0b111)) ## 7  int:转10进制
print(int(0o77))
print(hex(888))  #0x378  转16进制
print(hex(0o7777))
print(oct(0x13a))  ## 0o472  转8进制
print(oct(0x777))  ## 0o3567

print()
## 非零数都代表bool布尔真
print(bool(1))
print(bool(12))
print(bool(12.1)) ## True
print(bool(-3))   ## True
print(bool(0))   #False

print()
print(bool("qwe")) ## True
print(bool(""))  ##False

##基本上 非空都被认为是True
##空 都被认为是False   eg:"",[],{},None 都是False

##Python表示复数
print(2+36j)
print(type(2+3j))  ## <class 'complex'>

"let's go"  ##表示字符串的引号需要成对出现
'let"s"asdf" go'

# 'let's go'  ##这样表示是不行的
'let\'s go'  ## 转义字符

print('''   ##idle多行字符串
qwerg
qwegg
qweggggg
''')

print('\nqwerg\nqwegg\nqweggggg')

print('hello\
world')  ##helloworld

## 转义字符
# \n   换行
# \r   回车
# \t   横向制表符
# \'   单引号

print("hello \\n world")
print("c:\nasdf\rwer\nile") ##这样的\n处 会换行
print("c:\\nasdf\\rwer\\nile") ##这样正常显示\
print(r'asdfl\nasdf')  ##原始字符串

# print(r'let 's go ') ##这样还是不行 因为里面的不是一个合法的字符串 也就不存在合法的字符串
print("hello" + "world")
print("hello0"*3)
print("hello"[0])
print("hello"[3])
print("hello world"[-3])
print("hello world"[-6])
print("hello world"[-7])
print("hello world"[-5])
print("hello world"[6])
print("hello world"[0:5])
print("hello world"[0:-1])
print("hello world"[0:-3])
print("hello world"[6:])
print("hello world"[6:22])

print("hello world C# SWIFT java php python ruby"[:-4])
print("hello world C# SWIFT java php python ruby"[-4:])
print(R"C:\windows")