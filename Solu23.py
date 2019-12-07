# 23. 合并K个排序链表
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)

        pre = dummy
        for nn in lists:
            if len(nn) <1:
                lists.remove(nn)
        if len(lists) < 1:
            return dummy.next
        while len(lists) > 0:
            minn = 999999
            minNd = None
            for nd in lists:
                if nd.val < minn:
                    print(nd.val)
                    minNd = nd
                    minn = nd.val
            pre.next = minNd
            if minNd.next is not None:
                lists.append(minNd.next)
                minNd.next = None
                lists.remove(minNd)
            else:
                minNd.next = None
                lists.remove(minNd)

            pre = pre.next
            # if (minNd.next is not None):
            #     minNd = minNd.next
            #     # nextt = minNd.next
            #     # minNd.next = None
            #     # minNd = nextt
            # else:
            #     print("remove")
            #     lists.remove(minNd)
        return dummy.next
#Solution().mergeKLists([])

asdfgg = [[],[]]
for aa in asdfgg:
    print(aa is None)

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         import heapq
#         dummy = ListNode(0)
#         p = dummy
#         head = []
#         for i in range(len(lists)):
#             if lists[i] :
#                 heapq.heappush(head, (lists[i].val, i))
#                 lists[i] = lists[i].next
#         while head:
#             val, idx = heapq.heappop(head)
#             p.next = ListNode(val)
#             p = p.next
#             if lists[idx]:
#                 heapq.heappush(head, (lists[idx].val, idx))
#                 lists[idx] = lists[idx].next
#         return dummy.next