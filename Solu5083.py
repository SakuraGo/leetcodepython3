# 5083. Bigram 分词
#
# 示例
# 1：
# 输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
# 输出：["girl", "student"]



class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        res = []
        wordArrs = text.split(" ")
        lenss = len(wordArrs)
        print (wordArrs)
        for i in range(lenss-2):
            if (wordArrs[i] ==  first) & (wordArrs[i+1] == second ):
                print("a")
                res .append(wordArrs[i+2])
        return res

test =  Solution().findOcurrences("alice is a good girl she is a good student","a","good")
