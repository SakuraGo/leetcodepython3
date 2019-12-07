# 5206. 删除字符串中的所有相邻重复项 II  显示英文描述
# 用户通过次数 30
# 用户尝试次数 38
# 通过次数 30
# 提交次数 47
# 题目难度 Medium
# 给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
#
# 你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
#
# 在执行完所有删除操作后，返回最终得到的字符串。
#
# 本题答案保证唯一。

# 输入：s = "deeedbbcccbdaa", k = 3
# 输出："aa"
# 解释：
# 先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
# 再删除 "bbb"，得到 "dddaa"
# 最后删除 "ddd"，得到 "aa"

'''
可以使用stack 来处理，
一点点堆叠stack，发现stack顶有k个相同则出栈k个，继续到s的末尾

'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        print("s:",s)
        if len(s)<k:
            return s

        res = ""
        cnt = 0
        kpointLis = []
        for idx in range(0,len(s)):
            if idx == 0 or cnt == 0:
                cnt += 1
                continue
            if s[idx] == s[idx-1]:
                cnt += 1
                if cnt == k:
                    kpointLis.append(idx)
                    cnt = 0
            else:
                cnt = 1

        if len(kpointLis) == 0:
            return s
        else:
            startP = 0
            for idx in kpointLis:
                print("idx:",idx)
                res += s[startP:idx-k+1]
                startP = idx+1
                print("res:", res)
            res += s[startP:]

            return self.removeDuplicates(res,k)

res = Solution().removeDuplicates("deeedbbcccbdaa",3)
print(res)

