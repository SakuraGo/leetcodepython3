from  typing import List

## 空间复杂度爆炸。。
class MajorityChecker:  ##

    def __init__(self, arr: List[int]):
        self._arr = arr
        self._qianMemo = {}  ##以index为截至点的统计
        self._houMemo = {}  ##以index为起始点的统计  ##似乎用不到。。。用right - left 就是中间段的统计。。。

        for index, num in enumerate(self._arr):
            if index>0:
                self._qianMemo[index] = self._qianMemo[index-1].copy()
            else:
                self._qianMemo[index] = {}

            if num in self._qianMemo[index].keys():
                self._qianMemo[index][num] += 1
            else:
                self._qianMemo[index][num] = 1

    def query(self, left: int, right: int, threshold: int) -> int:
        if left == right:
            return self._arr[left]

        dicRight = self._qianMemo[right].copy()
        dicLeft = {}
        if left > 0:
            dicLeft = self._qianMemo[left-1].copy()
            print(dicRight)
            print(dicLeft)
            for num,cnt in dicLeft.items():    ###enumerate(dic.items())  会返回 index,(key,value)..
                                                ##### enumerate(dic)  返回 index,key
                print(num,cnt)
                dicRight[num] -= cnt

        print(dicRight)

        resLis = list(dicRight.items())
        print(resLis[1])
        resLis = sorted(resLis,key=lambda x:x[1] ,reverse= True)  ##这个sorted要有东西接收。。
        if resLis[0][1]>= threshold:
            return resLis[0][0]
        else:
            return -1


maj = MajorityChecker([1,1,2,2,1,1])
# print(maj.query(0,3,3))
# print(maj.query(0,5,4))
print(maj.query(2,3,2))











