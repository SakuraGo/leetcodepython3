from urllib import request

class Spider():
    url = "https://www.huya.com/l"

    def __fetch_content(self): ##私有方法..
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # print(htmls)
        print()

    def go(self):
        self.__fetch_content()



spider = Spider()
spider.go()

