from  typing import List
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        ucnt = 0
        rcnt = 0
        for c in command:
            if c == "U":
                ucnt += 1
            elif c == "R":
                rcnt += 1

        def getobs(x,y):
            xx = x // rcnt
            yy = y // ucnt
            dd = min(xx,yy)
            nx = x- dd * rcnt
            ny = y- dd * ucnt
            return [nx,ny]

        newObs = []
        # matrix = [[0 for j in range(rcnt + 1)] for i in range(ucnt + 1)]
        for obsx,obsy in obstacles:
            if obsx>x or obsy > y:
                continue
            ox,oy = getobs(obsx,obsy)
            if ox>rcnt or oy > ucnt:
                continue
            newObs.append([ox,oy])
            # matrix[oy][ox] = -1

        newx,newy = getobs(x,y)
        if newx > rcnt or newy > ucnt:
            return False
        touchFlag = False
        pos = [0,0]
        for c in command:
            if c == "U":
                pos[1] += 1
            else:
                pos[0] += 1
            if pos in newObs:
                return False
            if pos == [newx,newy]:
                touchFlag = True

        if touchFlag is True:
            return True
        else:
            return False

res = Solution().robot("URR",[[2, 2]], x = 3, y = 2)
print(res)