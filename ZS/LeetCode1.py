from typing import  List
class Solution:

    def game(self, guess: List[int], answer: List[int]) -> int:
        res = 0
        for i in range(3):
            if guess[i] == answer[i]:
                res += 1
        return res


'''
这次的题还是比较传统。首先简单说一下思路吧。

Problem 1
签到题， 一个一个挨个比较就行。
时间复杂度O(n), 空间复杂度O(n).

Problem 2
还是签到， 但是记住要将每一个分子分母取反并用gcd化简， 好在最后全是正数省略了许多判断。
时间复杂度O(nlog(max(n)),空间复杂度O(1).

Problem 3
这个题直接模拟的话会不知道什么时候停止。 而因为每次循环都会使得机器人向右和向上移动同样的格子数。经过若干次循环后， 我们可以将新的起点当做原点， 所有障碍物向左向下平移即可形成和初始状态相同（相似）的状态。
因此在开始的时候就可以判断机器人经过平移后每个障碍物是否会在机器人的路线上。只需要模拟一次就可以。
时间复杂度O(|command| ^ 2), 空间复杂度 O(|command| ^ 2).

Problem 4
这个是典型的轮廓线动态规划题目。 类似POJ2411。 每次放置考虑从上到下，从左至右放置。按照这种规律放的话， 每次放置，只需要记录从上一行的该格子到该格子前一个的状态。使用状态压缩转为2进制即可很方便使用dp进行转移。

Problem 5
感觉这个题比第四题还要简单一些。
这道题是在树上操作， 而每一次操作都只涉及单点和子树问题。 我们知道， 处理子树问题如果能把树化为一维数组来做就可以了。而很明显这道题使用DFS序列这种做法，先做一次DFS， 将每个点入栈和出栈的timestamp记录下来， 这个timestamp之间就是以该点为根的子树。将DFS序列作为新的序列，使用线段树就可以了。
时间复杂度 O(nlogn + qlogn), 空间复杂度 O(nlogn).

作者：haozheyan97
链接：https://leetcode-cn.com/circle/discuss/1I3IVg/view/WSfk3R/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''