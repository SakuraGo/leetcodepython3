origin = 0

def factory(pos):
    def go(step):
        nonlocal pos  ##强制声明不是本地局部变量，python就会往外找。
        print(id(pos))  ## pos在变.
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(id(tourist))#2782350962760
print(tourist(2))
print(tourist.__closure__[0].cell_contents)  #2
# print(origin)  #0
print(tourist(3))
print(id(tourist))#2782350962760
print(tourist.__closure__[0].cell_contents) #5 闭包记住了上一次的状态.
# print(origin) #0
print(tourist(6))
print(tourist.__closure__[0].cell_contents)
# print(origin) #0
# 2
# 5
# 11
print(id(tourist))#2782350962760 #tourist id没变