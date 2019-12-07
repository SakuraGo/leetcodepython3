# 451. 根据字符出现频率排序
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
#
# 输入:
# "tree"
#
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

# dict1={'a':2,'e':3,'f':8,'d':4}
# # list1= sorted(dict1.items(),key=lambda x:x[1],reverse=True)
# # print(list1)

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s)<1:
            return ""
        memoDic = {}
        for c in s:
            if c in memoDic.keys():
                memoDic[c] += 1
            else:
                memoDic[c] = 1
        lis = sorted(memoDic.items(),key= lambda x:x[1],reverse=True)
        res = ""
        for c ,cnt in lis:
            res  = res + c*cnt

        return res

res = Solution().frequencySort("tree")
print(res)





