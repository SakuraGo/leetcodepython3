from  typing import List

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self._arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:

        curLis = self._arr[left:right+1]

        ##找到出现次数最多的数 O(n)
        num = curLis[0]
        cnt = 1
        i = 1
        dic = {}
        while i < len(curLis):
            numi = curLis[i]
            if numi in dic.keys():
                dic[numi] += 1
            else:
                dic[numi] = 1

            if numi == num:
                cnt += 1
            elif cnt>0:

                cnt -= 1
            elif cnt == 0:
                num = numi
                cnt = 1
            i+= 1

        if dic[num] >= threshold:
            return num
        else:
            return -1



