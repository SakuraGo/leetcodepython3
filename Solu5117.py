# 5117.
# IP
# 地址无效化
#
#
#
# 示例
# 1：
#
# 输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        arrs = address.split('.')
        res = '[.]'.join(arrs)
        return res