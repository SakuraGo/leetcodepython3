class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        ts = []
        for t in transactions:
            name, stamp, amount, city = t.split(',')
            stamp = int(stamp)
            amount = int(amount)
            ts.append([name, stamp, amount, city, t])
        ans = set()
        for t in ts:
            if t[2] > 1000:
                ans.add(t[4])
            for o in ts:
                if t[0] == o[0] and abs(t[1] - o[1]) <= 60 and t[3] != o[3]:
                    ans.add(t[4])
        return list(ans)