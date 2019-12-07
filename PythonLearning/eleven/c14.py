
origin = 0

## 函数定义时，(也就是第一遍浏览但没有执行的时候。。)
## 等号左边的会被认为是自变量.. 不会再在向函数体外找这个量。。
##

def go(step):

    newpos = origin + step  ## UnboundLocalError: local variable 'origin' referenced before assignment
    # origin = newpos  ## 等号左边的会被认为是自变量.. 不会再在向函数体外找这个量。。这句不注释会报错
    return newpos
    # pass

print(go(2))
print(go(3))
print(go(6))

def come(step):
    global origin  ##解决方法使用global关键字..这样即使在=左边也会往外找。
    newPos = origin+step
    origin = newPos
    return newPos

print(come(2))
print(come(3))
print(come(6))