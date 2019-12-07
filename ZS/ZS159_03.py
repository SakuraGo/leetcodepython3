# 5232.
# 替换子串得到平衡字符串
# 显示英文描述
# 我的提交返回竞赛
#
# 有一个只含有
# 'Q', 'W', 'E', 'R'
# 四种字符，且长度为
# n
# 的字符串。
#
# 假如在该字符串中，这四个字符都恰好出现
# n / 4
# 次，那么它就是一个「平衡字符串」。
#
#
#
# 给你一个这样的字符串
# s，请通过「替换子串」的方式，使原字符串
# s
# 变成一个「平衡字符串」。
#
# 你可以用和「待替换子串」长度相同的
# 任何
# 其他字符串来完成替换。
#
# 请返回待替换子串的最小可能长度。
#
# 如果原字符串自身就是一个平衡字符串，则返回
# 0。

class Solution:
    def balancedString(self, s: str) -> int:
        alllen = len(s)
        biaozhun = alllen//4
        qcnt = 0
        wcnt = 0
        ecnt = 0
        rcnt = 0
        for c in s:
            if c == "Q":
                qcnt += 1
            elif c == "W":
                wcnt += 1
            elif c == "E":
                ecnt+= 1
            elif c == "R":
                rcnt += 1
        qcnt = max(qcnt-biaozhun,0)
        wcnt = max(wcnt - biaozhun, 0)
        ecnt = max(ecnt - biaozhun, 0)
        rcnt = max(rcnt - biaozhun, 0)
        targetLis = [qcnt,wcnt,ecnt,rcnt]
        print("target:",targetLis)
        curLis = [0,0,0,0] ## [q,w,e,r]
        if targetLis == curLis:
            return 0
        l ,r = 0,0
        minLen = len(s)
        def compaLis(lis,targetLis):
            return lis[0]>=targetLis[0] and lis[1]>=targetLis[1] and lis[2]>=targetLis[2] and lis[3]>=targetLis[3]

        while r <= len(s):
            print(l,r)
            if compaLis(curLis,targetLis): ##范围中字母数达到了需要改变的要求
                minLen = min(minLen,r-l)
                ##后续操作..#移动l
                c = s[l]
                idx = "QWER".find(c)
                curLis[idx] -= 1
                l+=1
                continue


            if compaLis(curLis,targetLis) is False and r<len(s):
                c = s[r]
                idx = "QWER".find(c)
                curLis[idx] += 1
                r +=1

                # print()
            elif compaLis(curLis,targetLis) is False and r >=len(s):
                break

        return minLen

res = Solution().balancedString("WWQQRRRRQRQQ")
print(res)

# q=1
# w=2
# e=3
# r=4
# targetLis = [q,w,e,r]
# print(targetLis)
#
# q = 33
# print(targetLis>[1,2,3,5])
# c = "W"
# idx = "QWER".find(c)
# print(idx)
#
# targetLis[2]-=35
# print(targetLis)
