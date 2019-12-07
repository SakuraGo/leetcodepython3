##可迭代对象
## 列表、元组、集合
## for in

# for in iterable
# 对象 class

class Book:
    pass

##把一个类变成可迭代的..
##迭代器 # Iterator
##一组书
class BookCollection:
    def __init__(self):
        self._data = ["《往事》","zhineng","huiwei"]
        self.cur = 0

    def __iter__(self):##需要实现这两个函数，就能把这个类变成可迭代的。
        return self

    def __next__(self):##需要实现这两个函数，就能把这个类变成可迭代的。
        if self.cur>= len(self._data):
            raise StopIteration()
        r = self._data[self.cur]
        self.cur += 1
        return r
        pass


asdff = {3,5,6}
for i in asdff:
    print(i)

asd = (3,5,6)
for a in asd:
    print(a)

import copy
# books_copy = books.copy() #'BookCollection' object has no attribute 'copy'
books = BookCollection()
books_copy = copy.copy(books)
for book in books:  ## for in 循环的实质就是一直在调用可迭代类的 __next__，取得下一个
    print("book:",book)                ## 直到遍历完了，返回异常。
books = BookCollection()
print(next(books))
print(next(books))
print(next(books))
# 《往事》
# zhineng
# huiwei
print("~~~~~~")


for book in books_copy:  ##第一次把迭代器用完了，不会再有打印输出
    print("book:",book)

lis  = [1,3,5,6]
for n in lis:
    print(n)
for n in lis: ##list可以再打印
    print(n)

