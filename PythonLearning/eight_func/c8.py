def demo(*param):##传入一个元组
    res = 0
    for i in param:
        res += i**2

    print(param)
    print(res)
demo(1,2,3,4,5,6)
demo(*[1,2,3,4,5,6])  ## *把列表平铺开来

def city_temp(**param):  ## **接受可变关键字参数
    print(param)
    print(type(param))  ## <class 'dict'>
    for k ,v in param.items():
        print(k,v)

    # for k,v ,c in param: ## not enough values to unpack (expected 3, got 2)
    #     print(k,":",v,c)


    for k in param:
        print(k)

    pass

print("~~~~~~~~~~")
city_temp(bj = "32c",xm = "23c",sh="31c")
dic = {"bj":"32c","sh":"23c"}
city_temp(**dic)   ##  **传入字典  *传入list 都是类似于平铺的作用

def kong(param1,**param):
    print(param1)
    for k ,v in param.items():
        print(k,v)

print("~~~~~~~~~~~~~~~")
kong(23,**dic)
kong("qwer",qwe=3,abc=4)
kong("qwer",**dic,gg="55555")