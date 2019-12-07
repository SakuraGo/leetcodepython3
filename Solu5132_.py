from typing import List
import queue

class NodeModel:
    def __init__(self,nodeIndex,isRed=True):
        self._nodeIndex = nodeIndex
        self._isRed = isRed  ##下一条线是否是红

class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        r_data = [None] * n
        b_data = [None] * n
        for i in range(n):
            lis = [0] * n
            r_data[i] = lis

        for i in range(n):
            lis = [0] * n
            b_data[i] = lis

        visited = [None] * n ##记录是否访问过
        for i in range(n):
            lis = [0] * 2   #[n][0] 被红线访问
            visited[i] = lis #[n][1] 被蓝线访问

        ord = [None] * n ##记录步数
        for i in range(n):
            lis = [-1] * 2    #[0] 红线至此步数
            ord[i] = lis     #[1] 蓝线到此步数

        q = queue.Queue()
        a = NodeModel(0,True) #下步红
        b = NodeModel(0,False) #下步蓝
        visited[0][0] = True
        visited[0][1] = True
        ord[0][0] = 0 #下步蓝
        ord[0][1] = 0 #下步红

        for data in red_edges:
            i,j  = data
            r_data[i][j] = 1
        for data in blue_edges:
            i,j = data
            b_data[i][j] = 1

        q.put(a)
        q.put(b)
        while q.empty() is False:
            x = q.get()
            nextFlag = x._isRed  ##下一条线的颜色是否为红
            curIndex = x._nodeIndex
            flag = 0
            if nextFlag is True:  ##下条线是红
                lis = r_data[curIndex]
                flag = 0  #0为被红线访问
            else:
                lis = b_data[curIndex]
                flag = 1
            for index,num in enumerate(lis):
                if num == 1:
                    if visited[index][flag] != 1: # 未被访问
                        visited[index][flag] = 1
                        ord[index][flag] = ord[curIndex][1-flag]+1
                        newNode = NodeModel(index,not nextFlag)
                        q.put(newNode)

            res = [-1] * n
            for i in range(n):
                a,b = ord[i]
                if a+b == -2:
                    continue
                else:
                    if a<0:
                        res[i] = b
                    elif b<0:
                        res[i] = a
                    else:
                        res[i] = min(a,b)


        return res


res= Solution().shortestAlternatingPaths(3,[[0,1],[1,2]],[])
print(res)














