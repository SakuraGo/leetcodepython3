# 5240. 串联字符串的最大长度  显示英文描述
# 用户通过次数 63
# 用户尝试次数 122
# 通过次数 65
# 提交次数 198
# 题目难度 Medium
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
#
# 请返回所有可行解 s 中最长长度。

from  typing import  List
class Solution:

    def isValid(self,s):
        cnt = [0]*26
        for c in s:
            idx = ord(c) - ord("a")
            cnt[idx] += 1
            if cnt[idx]>1:
                return False
        return True

    def maxLength(self, arr: List[str]) -> int:
        ##二进制组合推导
        dataKu = set()
        dataKu.add(0)
        for s in arr:
            erjinzhi = 0
            if self.isValid(s) is False: ##有重复的字母
                continue
            for c in s:
                erjinzhi += 1<<(ord(c)-ord("a"))
            for d in dataKu:
                print("d:",d)
            newDataKu= {data | erjinzhi  for data in dataKu if data&erjinzhi == 0}
            dataKu = dataKu.union(newDataKu)
        print(dataKu)
        res = 0
        for num in dataKu:
            res = max(res,bin(num).count("1"))
        return res
res = Solution().maxLength(["yy","bkhwmpbiisbldzknpm"])
print(res)



