# result

import queue
class Solution:
    def __init__(self):
        self._status = [0,0,0,0]

        self._pre = {}

    def findBestWay(self):
        qq = queue.Queue()
        qq.put('0000')
        memoSet = set()
        memoSet.add('0000')
        while qq.empty() is False:
            curStatus = qq.get()
            print(curStatus)
            newLis = []
            curMan = int(curStatus[0])
            man = int(curStatus[0])
            man = 1 - man

            for i in range(1,4):

                if int(curStatus[i]) == curMan:
                    newNum = 1 - int(curStatus[i])
                    newStatus = str(man) + curStatus[1:i] + str(newNum) + curStatus[i+1:]
                    newLis.append(newStatus)
                    print(newStatus)
                # else:

            shadoubudai = str(man) + curStatus[1:]
            newLis.append(shadoubudai)

            for status in newLis:
                if status in memoSet:
                    continue
                else:
                    if status == '1111':
                        self._pre[status] = curStatus
                        print("success!!")

                        ccc = status
                        while ccc is not '0000':
                            print(ccc)
                            ccc = self._pre[ccc]

                        print('0000')

                        return
                    memoSet.add(status)
                    manSta = int(status[0])
                    tempMax = 0
                    temp = 0
                    for i in range(1,4):
                        if int(status[i])==manSta:
                            temp = 0
                        else:

                            temp += 1
                            tempMax = max(tempMax, temp)

                    if tempMax>= 2:
                        ##有冲突
                        continue
                    else:
                        qq.put(status)  ##新的可能的路径
                        self._pre[status] = curStatus



res = Solution().findBestWay()







