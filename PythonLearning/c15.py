import t.t1.c9
print("~~~~~~~~~C15~~~~~~~~~")
print("name:",__name__)  ##名字
print("package:"+ (__package__ or "package不属于任何包"))  ## 所属包
print("doc:",__doc__)   ## 模块注释
print("file:",__file__)   ##物理路径

vvv  = 23 if 3>5 else  35
print(vvv)