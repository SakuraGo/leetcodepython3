# 5273. 搜索推荐系统  显示英文描述  我的提交返回竞赛
# 用户通过次数 68
# 用户尝试次数 90
# 通过次数 68
# 提交次数 103
# 题目难度 Medium
# 给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。
#
# 请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。
#
# 请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。
from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        leftLis = []
        for idx,c in enumerate(searchWord):
            for word in products:
                if (len(word)-1>= idx) and c == word[idx]:
                    leftLis.append(word)

            leftLis.sort()
            products = leftLis.copy()
            print(leftLis)
            if len(leftLis)>=3:
                res.append(leftLis[0:3])
            else:
                res.append(leftLis)
            leftLis = []
        return res


res = Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse")
print(res)