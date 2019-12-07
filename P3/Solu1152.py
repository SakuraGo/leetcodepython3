# 1152. 用户网站访问行为分析
# 为了评估某网站的用户转化率，我们需要对用户的访问行为进行分析，并建立用户行为模型。日志文件中已经记录了用户名、访问时间 以及 页面路径。
#
# 为了方便分析，日志文件中的 N 条记录已经被解析成三个长度相同且长度都为 N 的数组，分别是：用户名 username，访问时间 timestamp 和 页面路径 website。第 i 条记录意味着用户名是 username[i] 的用户在 timestamp[i] 的时候访问了路径为 website[i] 的页面。
#
# 我们需要找到用户访问网站时的 『共性行为路径』，也就是有最多的用户都 至少按某种次序访问过一次 的三个页面路径。需要注意的是，用户 可能不是连续访问 这三个路径的。
#
# 『共性行为路径』是一个 长度为 3 的页面路径列表，列表中的路径 不必不同，并且按照访问时间的先后升序排列。
#
# 如果有多个满足要求的答案，那么就请返回按字典序排列最小的那个。（页面路径列表 X 按字典序小于 Y 的前提条件是：X[0] < Y[0] 或 X[0] == Y[0] 且 (X[1] < Y[1] 或 X[1] == Y[1] 且 X[2] < Y[2])）
#
# 题目保证一个用户会至少访问 3 个路径一致的页面，并且一个用户不会在同一时间访问两个路径不同的页面。

from  typing import  List

class MemoModel:
    def __init__(self,name,timeStamp,website):
        self._name = name
        self._time = timeStamp
        self._web = website

class Solution:

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        memo = []

        lenn = len(username)

        for i in range(lenn):
            model = MemoModel(username[i],timestamp[i],website[i])
            memo.append(model)

        memo.sort(key= lambda x:x._time)

        diccc = {}

        for mm in memo:
            print(mm)
            name = mm._name
            web = mm._web
            if name not in diccc.keys():
                diccc[name] = [web]
            else:
                diccc[name].append(web)

        shunxuLis = []



        for name,webs in diccc.items():
            temp = set()
            for web in webs:
                temp = temp | {web}

            def dfs(self, allCombine: List, curCombine: List, curIndex: int):
                if len(curCombine) == 3:
                    temp.add(curCombine)




        return ["q"]



# asd = set()
# asd.add(1)
# asd.add([1,2])

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        n = len(timestamp)
        dic = {}
        for i in range(n):
            if username[i] not in dic:
                dic[username[i]] = []
            dic[username[i]].append((timestamp[i], website[i]))
        for k in dic.keys():
            dic[k] = [i[1] for i in sorted(dic[k], key = lambda x: x[0])]
        count_dic = {}
        for name in dic.keys():
            arr = dic[name]
            l = len(arr)
            if l <= 2:
                continue
            visited = set()
            for i in range(l):
                for j in range(i+1, l):
                    for w in range(j+1, l):
                        if (arr[i],arr[j],arr[w]) not in count_dic:  ### set中不能有List 但是可以有元组！
                            count_dic[(arr[i],arr[j],arr[w])] = 0
                        if (arr[i],arr[j],arr[w]) not in visited:
                            visited.add((arr[i],arr[j],arr[w]))
                            count_dic[(arr[i],arr[j],arr[w])]+=1
        ans = []
        v = max(count_dic.values())
        for k in count_dic.keys():
            if count_dic[k] == v:
                ans.append(k)
        ans.sort()
        return ans[0]