# 898. 子数组按位或操作
# 我们有一个非负整数数组 A。
#
# 对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），我们对 B 中的每个元素进行按位或操作，获得结果 A[i] | A[i+1] | ... | A[j]。
#
# 返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）

# 输入：[1,1,2]
# 输出：3
# 解释：
# 可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
# 产生的结果为 1，1，2，1，3，3 。
# 有三个唯一值，所以答案是 3 。

from typing import List

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        memo = [None] * len(A)
        for i in range(len(A)):
            arr = [0]*len(A)
            memo[i] = arr
            memo[i][i] = A[i]

        tempRes = set(A.copy())
        for i in range(len(memo)):
            for j in range(i+1,len(memo[0])):
                memo[i][j] = A[j] | memo[i][j-1]
                if memo[i][j] in tempRes:
                    continue
                else:
                    tempRes.append(memo[i][j])
        return len(tempRes)

'''
 ###这个方法比我的N2复杂度的动态规划优势的地方在于，N2复杂度计算中存在很多重复的数。。
 ##除非是1,2,4,8.。。。这种情况下，计算量是相同的    
##而这个方法使用了set，使得每一步如果有重复的数出现，也会被合并成一个。不浪费计算量                              
    
class Solution:
    def subarrayBitwiseORs(self, A):
        cur = set()      
        res = set()        
        for a in A:
            cur = {n | a for n in cur} | {a}       ##记录以当前数为结尾的 所有可能的数的set   
            res |= cur                             ##记录所有的数 set 
        return len(res)
这是一种空间换时间的做法，一个cur集合储存上一次循环的位或结果集合，
将这些集合和当前循环的元素进行位或运算，在补充上当前元素。然后一个res和cur取并集。 
为什么要有一个cur而不直接用res呢？或者为什么要用两个集合而不是一个集合呢？
考虑[1，2，4]这个测试用例:
第一轮循环时，a=1,cur={1},res={1}
第二轮循环时，a=2,cur = {1|2}|{2} = {2,3}, res={1,2,3}
第三轮循环时，a=4,cur={2|4, 3|4}|{4} = {4, 6, 7},res={1,2,3,4,6,7}
那么显然直接返回cur的长度是不可能的，直接返回cur和原始输入A的并集也是不可以的，因为漏掉了3。
对于我能考虑到替换res的两种方法，都会导致测试不通过，所以res这个集合的存在是有必要的。

'''

s1 = set([1,2,3])
s1.add(1)
s1.add(35)
print(s1)
