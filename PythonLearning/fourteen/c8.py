class Test():
    # pass
    def __bool__(self):
        print("bool called")
        return True  ##导致bool(Test())为False

    def __len__(self):
        # return "8" #TypeError: 'str' object cannot be interpreted as an integer
        # return 8.0 #TypeError: 'float' object cannot be interpreted as an integer
        print("lllen called")
        return False #这个可以
        # return False #这个也可以

print(bool(Test()))  #如果class 内部__bool__不出现，将以__len__的返回结果作为判断依据
print("~~~~")
print(len(Test()))  #True:1   False:0

