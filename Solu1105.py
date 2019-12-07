# 1105. 填充书架  显示英文描述
# 用户通过次数 17
# 用户尝试次数 29
# 通过次数 17
# 提交次数 35
# 题目难度 Medium
# 附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。
#
# 你把要摆放的书 books 都整理好，叠成一摞：从上往下，第 i 本书的厚度为 books[i][0]，高度为 books[i][1]。
#
# 按顺序 将这些书摆放到总宽度为 shelf_width 的书架上。
#
# 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelf_width），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
#
# 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
#
# 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
#
# 以这种方式布置书架，返回书架整体可能的最小高度。
# 输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# 输出：6
# 解释：
# 3 层书架的高度和为 1 + 3 + 2 = 6 。
# 第 2 本书不必放在第一层书架上。


from typing import List
# class Solution:
#     def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        ans = [1 << 31] * (n + 1)   ##memo
        ans[0] = 0
        for i in range(1, n + 1):
            temp = 0
            index = i
            h = 0
            while index > 0:    ##因为书本排序固定，只是每本书到底与上面的书排一起还是后续的书排一起不确定，因此可以做dp
                ##dp时每加一本书，理论上可以往前合并到一层，直到合并的书的宽度超出书架宽度。。。
                temp += books[index - 1][0]
                if temp > shelf_width:
                    break
                h = max(h, books[index - 1][1])
                ans[i] = min(ans[i], ans[index - 1] + h)   ##选择这本书，+h ，因为每本书都要排列
                index -= 1
        return ans[n]



qwe = Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],4)
print(qwe)