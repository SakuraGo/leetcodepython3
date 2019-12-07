# 1153. 字符串转化  显示英文描述
#
# 给出两个长度相同的字符串，分别是 str1 和 str2。请你帮忙判断字符串 str1 能不能在 零次 或 多次 转化后变成字符串 str2。
#
# 每一次转化时，将会一次性将 str1 中出现的 所有 相同字母变成其他 任何 小写英文字母（见示例）。
#
# 只有在字符串 str1 能够通过上述方式顺利转化为字符串 str2 时才能返回 True，否则返回 False。​​

# 输入：str1 = "aabcc", str2 = "ccdee"
# 输出：true
# 解释：将 'c' 变成 'e'，然后把 'b' 变成 'd'，接着再把 'a' 变成 'c'。注意，转化的顺序也很重要。

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        dic1 = {}  ##保存某个字母与该字母出现过的index

        set2 = set() ## 作用是查找str2中是否满了26个字母，如果满了的话，再怎么变换都不可能顺利转变。会带偏一个字母
        for i in range(len(str1)):

            if str1[i] in dic1.keys():
                dic1[str1[i]].append(i)
            else:
                dic1[str1[i]] = [i]
            set2.add(str2[i])

        if len(set2) == 26: ##26个字母，没有操作空间。。
            return False
        print(dic1)
        print(set2)

        for item in dic1.items():
            _ ,lis = item
            c = str2[lis[0]]
            print(c)
            for index in lis:   ## 查看某个字母对应的序号上的字母是否都是同一个。。如果不是同一个，aaa是不可能变成 bcd 的,因为3个a要一起变
                if c == str2[index]:
                    continue
                else:
                    return False

        return True


res = Solution().canConvert("leetcode","codeleet")
print(res)