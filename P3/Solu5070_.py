from  typing import  List
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        memo = [[99999 for _ in range(len(colors))] for j in range(3)]
        # print(memo)
        onePos = -99999
        twoPos = -99999
        threePos = -99999
        for idx,c in enumerate(colors):
            if c == 1:
                onePos = idx
            elif c == 2:
                twoPos = idx
            else:
                threePos = idx
            memo[0][idx] = min(memo[0][idx], idx-onePos)
            memo[1][idx] = min(memo[1][idx], idx - twoPos)
            memo[2][idx] = min(memo[2][idx], idx - threePos)

        onePos = 99999
        twoPos = 99999
        threePos = 99999

        for idx in range(len(colors)-1,-1,-1):
            c = colors[idx]
            if c == 1:
                onePos = idx
            elif c ==2 :
                twoPos = idx
            else:
                threePos = idx
            memo[0][idx] = min(memo[0][idx],onePos - idx)
            memo[1][idx] = min(memo[1][idx], twoPos - idx)
            memo[2][idx] = min(memo[2][idx], threePos - idx)

        res = []

        for q in queries:
            juli = memo[q[1]-1][q[0]]
            if juli >9999:
                res.append(-1)
            else:
                res.append(juli)
        return res

res = Solution().shortestDistanceColor([2,3],[1,2])