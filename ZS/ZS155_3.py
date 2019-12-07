# 5199. 交换字符串中的元素  显示英文描述  我的提交返回竞赛

# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
#
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
#
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

from  typing import List
class Solution:
    ##并查集考察。。
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ##
        father = [i for i in range(len(s))]
        def getFather(idx):
            if father[idx] != idx:
                father[idx] = getFather(father[idx])
            return father[idx]

        ## 合并
        for x,y in pairs:
            fax = getFather(x)
            fay = getFather(y)
            if fax == fay:
                continue
            else:
                father[getFather(x)] = getFather(y)

        memo = {}
        for i in range(len(s)):
            if getFather(i) in memo.keys():
                memo[getFather(i)].append((i,s[i]))
            else:
                memo[getFather(i)] = [(i,s[i])]

        res_list = ["" for i in range(len(s))]
        for key,value in memo.items():
            print("key:",key)
            indicies = []
            chars = []
            for idx,char in value:
                indicies.append(idx)
                chars.append(char)
            indicies.sort()
            print("indicies:",indicies)
            chars.sort()
            print("chars:",chars)
            for j in range(len(indicies)):
                print("j:",j)
                res_list[indicies[j]] = chars[j]
                # print()
        res  = "".join(res_list)
        return res

res = Solution().smallestStringWithSwaps("dcab",[[0,3],[1,2],[0,2]])
print(res)



# sss = "qwer"
# sss[2] = "e"  ## 字符串不能这么改变某个index位置的值。。TypeError: 'str' object does not support item assignment
# print(sss)
















'''
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        fa = [0]*len(s)
        res_list = ['']*len(s)
        def getfa(a):
            if fa[a]!=a:
                fa[a] = getfa(fa[a])
            return fa[a]

        for i in range(0,len(s)):
            fa[i] = i

        p_tree = defaultdict(list)
        for x,y in pairs:
            fax = getfa(x)
            fay = getfa(y)
            if fax!=fay:
                fa[fax] = fay

        for i in range(0,len(s)):
            fai = getfa(i)
            p_tree[fai].append([i,s[i]])

        for key,value_info in p_tree.items():
            index_list = [x[0] for x in value_info]
            value_list = [x[1] for x in value_info]
            value_list.sort()
            index_list.sort()
            # print(value_list,index_list)
            for index,value in zip(index_list,value_list):
                res_list[index] = value
        return ''.join(res_list)
'''