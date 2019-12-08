# 5082. 矩阵中 1 的最大数量  显示英文描述
# 通过次数 13
# 提交次数 87
# 题目难度 Hard
# 现在有一个尺寸为 width * height 的矩阵 M，矩阵中的每个单元格的值不是 0 就是 1。
#
# 而且矩阵 M 中每个大小为 sideLength * sideLength 的 正方形 子阵中，1 的数量不得超过 maxOnes。
#
# 请你设计一个算法，计算矩阵中最多可以有多少个 1。

# 输入：width = 3, height = 3, sideLength = 2, maxOnes = 1
# 输出：4
# 解释：
# 题目要求：在一个 3*3 的矩阵中，每一个 2*2 的子阵中的 1 的数目不超过 1 个。
# 最好的解决方案中，矩阵 M 里最多可以有 4 个 1，如下所示：
# [1,0,1]
# [0,0,0]
# [1,0,1]

# 1 <= width, height <= 100
# 1 <= sideLength <= width, height
# 0 <= maxOnes <= sideLength * sideLength

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:


        if maxOnes == 0 :
            return 0
        ##当前思路：每个正方形从左上角开始变1，横向加或是纵向加看width与height哪个比较小。 可能会超时？？


