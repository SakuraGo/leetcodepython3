from typing import List
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self._arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:

        curLis = self._arr[left:right + 1]

        ##找到出现次数最多的数 O(n)
        i = 0
        dic = {}
        while i < len(curLis):
            num = curLis[i]
            if num in dic.keys():
                dic[num] += 1

            else:
                dic[num] = 1

            if dic[num] >= threshold:
                return num
        return  -1


