# # 86. 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head
        if head is None:
            return head
        while  pre.next is not None and pre.next.val < x:
            print(pre.val)
            pre = pre.next

        if pre.next is None:
            return head

        flag = pre.next
        pre11 = flag
        cur = flag.next
        while cur is not None:
            print(cur.val)
            if cur.val >= x:
                pre11 = cur
                cur = cur.next

            else:
                pre.next = cur
                pre11.next = cur.next
                cur.next = flag
                cur = pre11.next
                pre = pre.next

        return dummy.next
