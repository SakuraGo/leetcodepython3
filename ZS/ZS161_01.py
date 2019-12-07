# 5247. 交换字符使得字符串相同  显示英文描述
# 用户通过次数 238
# 用户尝试次数 325
# 通过次数 239
# 提交次数 474
# 题目难度 Easy
# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。
#
# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
#
# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
#
# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ycnt = 0
        upcnt = 0
        downcnt = 0
        for idx in range(len(s1)):
            if s1[idx] == "y" and s2[idx] == "y":
                # 相同 不需处理
                continue
            if s1[idx] == "y" and s2[idx] == "x":
                ycnt += 1
                upcnt += 1
                continue
            if s1[idx] =="x" and s2[idx] =="y":
                ycnt += 1
                downcnt += 1
                continue
            if s1[idx] == "x" and s2[idx] == "x":
                #不需处理
                continue

        if ycnt%2 == 1:
            return -1
        res = 0
        res += (upcnt//2)
        res += (downcnt//2)
        res += (upcnt%2)
        res += (downcnt%2)
        return res