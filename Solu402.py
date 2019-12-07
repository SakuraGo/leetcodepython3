# str = "012345"
# a = int(str)
# print(a)
# l = len(str)
# k=1
# str = str[0:k]+str[k+1:l]
# print(str)
# 贪心算法主要是要找到相对应的贪心策略。假设每次只移除一位后达到所有可能的最小值，利用这个策略移除至k位，就是结果。
#
# 如num = "1432219", k = 3; 先移除一位变成所有可能最小，变成"132219"; 再对移除后的最小字符串移除一位变成所有可能最小，变成"12219"; 再对移除后的最小字符串移除一位变成所有可能最小，变成"1219"。
#
# 由此试出了相应的贪心策略, 就是如果当前字符小于后一个字符，那么就移除当前字符，然后将当前字符前面的字符串和后面的字符串拼接成新的字符串，就是移除一位后的最小结果，递归进行该行为，直到k次。
#
# 如"1432219"，移除一位，使得结果是所有可能最小，明显'4' > '3'，那么移除'4'，拼接成的字符串为"132219"，移除k位就进行k次相同过程。
#
# 不过这种递归过程效率低，可以采用开辟一个数组或者栈进行迭代，如果遍历到的当前字符比数组或栈中最后一个字符小就弹出，直到当前字符大于栈顶字符就添加入栈
import math
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         for i in range(k):
#             l = len(num)
#             if (l<=1):
#                 return "0"
#
#             min = int(num)
#             for j in range(l):
#
#                 subNum = num[0:j] + num[j+1:l]
#                 print(subNum)
#                 if int(subNum)<min:
#                     min = int(subNum)
#
#             num = str(min)
#
#         return num

# 先看只去掉一个数的时候，如何使得变得最小。。
# 上面是自己弄的，暴力解法。
# 应该是从头开始遍历，一旦发现index的下一个数字比index小的时候，删去index的数字。。
# 如果遍历到末尾都是递增的话，就删掉末尾的数字。。

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        lens = len(num)
        j = 0

        if (k >= lens):
            return '0'

        stack = list(num)

        for _ in range(k):
            while (j < len(stack) - 1 and stack[j] <= stack[j + 1]):
                j += 1
            stack.pop(j)
            j = max(0, j - 1)
        result = ''.join(stack).lstrip('0')
        return result if result else '0'

ssd = Solution().removeKdigits('189210',2)