# 圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。
#
# 给你两个整数 tomatoSlices 和 cheeseSlices，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：
#
# 巨无霸汉堡：4 片番茄和 1 片奶酪
# 小皇堡：2 片番茄和 1 片奶酪
# 请你以 [total_jumbo, total_small]（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量都是 0。
#
# 如果无法使剩下的番茄片 tomatoSlices 和奶酪片 cheeseSlices 的数量为 0，就请返回 []。


# 设巨无霸汉堡有
# xx
# 个，皇堡有
# yy
# 个，由于所有的材料都需要用完，因此我们可以得到二元一次方程组：
#
# \begin
# {cases}
# 4
# x + 2
# y = \text
# {tomatoSlices} \\ x + y = \text
# {cheeseSlices} \end
# {cases}
# {
#     4
# x + 2
# y = tomatoSlices
# x + y = cheeseSlices
# ​

#
# class Solution:
#     def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
#         if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2 or cheeseSlices * 4 < tomatoSlices:
#             return []
#         return [tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2]
#
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients/solution/bu-lang-fei-yuan-liao-de-yi-bao-zhi-zuo-fang-an-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。