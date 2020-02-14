# 5334. 推文计数  显示英文描述
#
# 请你实现一个能够支持以下两种方法的推文计数类 TweetCounts：
#
# 1. recordTweet(string tweetName, int time)
#
# 记录推文发布情况：用户 tweetName 在 time（以 秒 为单位）时刻发布了一条推文。
# 2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)
#
# 返回从开始时间 startTime（以 秒 为单位）到结束时间 endTime（以 秒 为单位）内，每 分 minute，时 hour 或者 日 day （取决于 freq）内指定用户 tweetName 发布的推文总数。
# freq 的值始终为 分 minute，时 hour 或者 日 day 之一，表示获取指定用户 tweetName 发布推文次数的时间间隔。
# 第一个时间间隔始终从 startTime 开始，因此时间间隔为 [startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>，其中 i 和 delta（取决于 freq）都是非负整数。

from typing import List
import math
class TweetCounts:

    def __init__(self):
        self._dataBase = {}


    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self._dataBase:
            self._dataBase[tweetName].append(time)
        else:
            self._dataBase[tweetName] = [time]


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        deltaa = 60
        if freq == 'hour':
            deltaa = 3600
        elif freq == 'day':
            deltaa = 86400


        ##先构造再填充
        shijianduans = math.ceil((endTime - startTime+1)/deltaa)
        res = [0]*shijianduans

        data = self._dataBase[tweetName]

        for time in data:
            if time<startTime:
                continue
            if time>endTime:
                continue

            idx = (max(0,time-startTime))//deltaa
            res[idx]+=1

        print(res)
        return res

# ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
# [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

obj = TweetCounts()
obj.recordTweet("tweet3",0)
obj.recordTweet("tweet3", 60);
obj.recordTweet("tweet3", 10);
obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 59);
obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 60);
















# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)