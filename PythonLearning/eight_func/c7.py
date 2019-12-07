#
# print("a","b","c")

## 可变参数列表
   ## 必须参数， 默认参数，可变参数
def demo(param1,param2 = 352,*param):
    print(param1)
    print(param2)
    print(param)
    ##默认把param组装成tuple
    # print(type(param))

demo(1,2,3,5,6,7)

demo((1,2,3,4,5,6)) ##  这样做会使得param成为一个二维元组

a = (1,2,3,4,5,6)
demo(*a)  ##一维元组  # *a 的作用就是把 元组a的元素平铺开传入demo中去

demo("a",23,55,5)
print("momo")
# demo("a",*param = (23,55,5))
def momo(param1,*param,param2 = 352):
    print(param1)
    print(param2)
    print(param)
    ##默认把param组装成tuple
    # print(type(param))

momo("a",1,2,3,"param22") # *param吃掉了“a”后所有的元素..
momo("aaqwer a",1,2,3,param2="param22")