# 5167. 查询无效交易  显示英文描述
#
# 如果出现下述两种情况，交易 可能无效：
#
# 交易金额超过 ¥1000
# 或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整）
# 每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。
#
# 给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。


from typing import  List
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        memoDic = {}

        for index,content in enumerate(transactions):
            conArr = content.split(",")
            name,time,amount,city = conArr
            if int(amount)>1000:
                res .append(content)
            else:
                if name in memoDic.keys():
                    memoDic[name].append((time,index))
                else:
                    memoDic[name] = [(time,index)]
        zongLis = []
        for key,arr in memoDic.items():
            sArr =sorted(arr,key= lambda x : x[0])
            temp = set()
            for i in range(0,len(sArr)-1):
                if int(sArr[i][0])>= int(sArr[i+1][0]) - 60:
                    temp.add(i)
                    temp.add(i+1)

            zongLis += list(temp)

        for index in zongLis:
            res.append(transactions[index])

        return res

res = Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])

print(res)