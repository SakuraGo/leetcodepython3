# 5149. 快照数组
# 实现支持下列接口的「快照数组」- SnapshotArray：
#
# SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。
# void set(index, val) - 会将指定索引 index 处的元素设置为 val。
# int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
# int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。

# 输入：["SnapshotArray","set","snap","set","get"]
#      [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5

# 提示：
#
# 1 <= length <= 50000
# 题目最多进行50000 次set，snap，和 get的调用 。
# 0 <= index < length
# 0 <= snap_id < 我们调用 snap() 的总次数
# 0 <= val <= 10^9
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
from typing import List

class SnapshotArray:

    def __init__(self, length: int):
        self._memo = {}
        for i in range(length):
            self._memo[i] = []   ##保存每个索引位置上的改变信息 (snapID,val)
        self._cache = {}
        self._data = [0] * length
        self._snapID = 0

    def set(self, index: int, val: int) -> None:
        self._data[index] = val
        self._cache[index] = val


    def snap(self) -> int:
        for ind,val in self._cache.items():
            self._memo[ind].append((self._snapID,val))
        self._cache = {}
        self._snapID += 1
        return self._snapID - 1

    def erfenSousuo(self,lis:List,snapid:int):
        if (len(lis)==1):
            if snapid>= lis[0][0]:
                return lis[0][1]
            else:
                return 0
        if (len(lis)== 2) :
            if snapid >= lis[1][0]:
                return lis[1][1]
            else:
                return self.erfenSousuo(lis[0:1],snapid)
        left = 0
        right = len(lis) - 1
        mid = len(lis) // 2
        # print(mid,right)
        if snapid > lis[mid][0]:
            return self.erfenSousuo(lis[mid:right+1],snapid)
        elif snapid < lis[mid][0]:
            return self.erfenSousuo(lis[left:mid],snapid)
        else: # ==
            return lis[mid][1]


    def get(self, index: int, snap_id: int) -> int:
        # print("---",self._snapID)
        if len(self._memo[index])>0:
            return self.erfenSousuo(self._memo[index],snap_id)
        return 0

#
# obj = SnapshotArray(3)
# obj.set(0,5)
# param_2 = obj.snap()
# param_3 = obj.get(0,0)
# print(param_3)
# #
# dic = {1:11}
# dic[1] = 123
# dic[3] = 33
#
# print(dic)
# print(dic.items())

["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
[[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
obj = SnapshotArray(1)

obj.snap()
obj.snap()
obj.set(0,4)
obj.snap()
obj.get(0,1)
obj.set(0,12)
obj.get(0,1)
obj.snap()
obj.get(0,3)


'''
class SnapshotArray(object):

    def __init__(self, length):

        self.arr = [[0] for _ in xrange(length)]
        self.time = [[0] for _ in xrange(length)]
        self.count = 0

    def set(self, index, val):

        if self.count == self.time[index][-1]:
            self.arr[index][-1] = val
            return
        self.arr[index].append(val)
        self.time[index].append(self.count)
        # print self.arr, self.time

    def snap(self):
        self.count += 1
        return self.count - 1

    def get(self, index, snap_id):
        pick = bisect.bisect_left(self.time[index], snap_id)
        if pick >= len(self.arr[index]):
            return self.arr[index][-1]
        if self.time[index][pick] > snap_id:
            pick -= 1
            if pick < 0:
                pick += 1
        return self.arr[index][pick]
'''
'''
/// Binary Search
/// Time Comnplexity: init: O(n)
///                   set: O(1)
///                   snap: O(1)
///                   get: O(log(calls))
class SnapshotArray {

private:
    vector<vector<pair<int, int>>> data;
    int id = 0;

public:
    SnapshotArray(int length) {

        data.resize(length);
        for(int i = 0; i < length; i ++)
            data[i].push_back(make_pair(-1, 0));
    }

    void set(int index, int val) {
        data[index].push_back(make_pair(id, val));
    }

    int snap() {
        return id ++;
    }

    int get(int index, int snap_id) {

        if(!data[index].size()) return 0;
        auto iter = lower_bound(data[index].begin(), data[index].end(), make_pair(snap_id + 1, INT_MIN));
        iter --;
        return iter->second;
    }
};
'''
