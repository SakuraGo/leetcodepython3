# 5061. 设计文件系统
#
# 你需要设计一个能提供下面两个函数的文件系统：
#
# create(path, value): 创建一个新的路径，并尽可能将值 value 与路径 path 关联，然后返回 True。如果路径已经存在或者路径的父路径不存在，则返回 False。
# get(path): 返回与路径关联的值。如果路径不存在，则返回 -1。
# “路径” 是由一个或多个符合下述格式的字符串连接起来形成的：在 / 后跟着一个或多个小写英文字母。
#
# 例如 /leetcode 和 /leetcode/problems 都是有效的路径，但空字符串和 / 不是有效的路径。
#
# 好了，接下来就请你来实现这两个函数吧！（请参考示例以获得更多信息）

class FileSystem:

    def __init__(self):
        self._memoDic = {}

    def create(self, path: str, value: int) -> bool:
        if path in  self._memoDic.keys():
            return False
        pathArr= path.split('/')
        if len(pathArr[0]) == 0:
            pathArr.pop(0)
        if len(pathArr) == 1 and len(pathArr[0])>0:
            self._memoDic[path] = value
            return True

        fatherPath = ''
        for p in pathArr[:-1]:
            if len(p) == 0:
                return False
            else:
                fatherPath += '/'
                fatherPath += p
        if fatherPath not in  self._memoDic.keys():
            return False
        else:
            self._memoDic[path] = value
            return True

    def get(self, path: str) -> int:

        if path in self._memoDic.keys():
            return self._memoDic[path]
        else:
            return -1

#
# asdf= ["a","b","d"]
# for i in asdf[:-1]:
#     print(i)


# ["FileSystem","create","create","get","create","get"]
# [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
obj = FileSystem()
param_1 = obj.create("/leet",1)
param_2 = obj.create("/leet/code",2)
print(param_2)