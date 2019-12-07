# 你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1  变成字母 I 。
#
# 如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。
#
# 给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。

class Solution:
    def toHexspeak(self, num: str) -> str:
        ssset = set()
        ssset = set(["A","B","C","D","E","F","I","O"])
        num16 = hex(int(num))
        num16 = num16[2:]
        num16 = num16.upper()
        num16=num16.replace("1","I")
        num16 = num16.replace("0","O")
        print(num16)
        for c in num16:
            if c not in ssset:
                print(c)
                return "ERROR"

        return num16

asd = Solution().toHexspeak("257")
print(asd)