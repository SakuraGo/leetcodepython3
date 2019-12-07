def demo():
    global  c  ## 全局变量c 可在函数外调用
    c = 222


demo() ##需要调用一下才能使得c成为global

print(c)
