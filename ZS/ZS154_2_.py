class Solution:

    def revvv(self,subStr,flag):
        res = ""
        biaoji = 0
        kuohao = []
        fenge = []
        for idx,c in enumerate(subStr):
            if c == "(":
                kuohao.append(idx)
            elif c == ")":
                qian = kuohao.pop()
                if len(kuohao) == 0:
                    fenge.append((qian,idx))

        if len(fenge) == 0:
            if flag == 1:
                print("substr111:",subStr)
                return subStr
            else:
                print("substr000:", subStr)
                return subStr[::-1]

        if flag == 1:
            lastIdx = 0
            res = ""
            for qIdx,pIdx in fenge:
                res += subStr[lastIdx:qIdx]
                res += self.revvv(subStr[(qIdx+1):pIdx],1-flag)
                lastIdx = pIdx+1
            res += subStr[lastIdx:][::-1]
            # print(res)
            return res
        else:
            lastIdx = len(subStr)-1
            res = ""
            for i in range(len(fenge)):
                qIdx,pIdx = fenge[len(fenge)-i-1]
                res += subStr[(pIdx+1):lastIdx+1][::-1]
                res += self.revvv(subStr[(qIdx+1):pIdx],1-flag)
                lastIdx = qIdx - 1
            res += subStr[0:lastIdx+1]
            # print(res)
            return res



    def reverseParentheses(self, s: str) -> str:

        return self.revvv(s,1)
## "ta()usw((((a))))"
res = Solution().reverseParentheses("ta()usw((((a))))")
print(res)

# stackk = []
#
# asdf = "qwergggg"
# print(asdf[2:6][::-1])