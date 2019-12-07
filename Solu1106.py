# 1106. 解析布尔表达式  显示英文描述
# 用户通过次数 43
# 用户尝试次数 48
# 通过次数 43
# 提交次数 57
# 题目难度 Hard
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
#
# 有效的表达式需遵循以下约定：
#
# "t"，运算结果为 True
# "f"，运算结果为 False
# "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
# "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
# "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
# 输入：expression = "!(f)"
# 输出：true
# 输入：expression = "|(&(t,f,t),!(t))"
# 输出：false

class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        if exp=="t":
            return True
        if exp=="f":
            return False
        if exp[0]=="!":
            return self.parseBoolExpr(exp[2:len(exp)-1])==False
        if exp[0]=="&":
            las=2;p=2;n=len(exp)
            now=True;tot=0
            while p<n:
                if exp[p]=="(":
                    tot+=1
                if exp[p]==")":
                    tot-=1
                if exp[p]=="," and tot==0:
                    now&=self.parseBoolExpr(exp[las:p])
                    las=p+1
                p+=1
            now&=self.parseBoolExpr(exp[las:n-1])
            return now
        if exp[0]=="|":
            las=2;p=2;n=len(exp)
            now=False;tot=0
            while p<n:
                if exp[p]=="(":
                    tot+=1
                if exp[p]==")":
                    tot-=1
                if exp[p]=="," and tot==0:
                    now|=self.parseBoolExpr(exp[las:p])
                    las=p+1
                p+=1
            now|=self.parseBoolExpr(exp[las:n-1])
            return now

res = Solution().parseBoolExpr("&(t,t,f)")
print(res)