class Test():
    pass

##一个实例化对象 #
test = Test()
print(test) ##<__main__.Test object at 0x000001586047A240>
if test:
    print("S") #走了这里
else:
    print("F")


class TestNone():
    # pass
    def __len__(self):
        return 0

test2 = TestNone()
print(test2) # <__main__.TestNone object at 0x000001DF7FCAA470>
if test2:
    print("s2")
else:
    print("f2") ##走了这里。。

print(bool(None)) #False
print(bool([])) #False
print(bool(test2)) #False