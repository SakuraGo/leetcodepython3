# 82. 删除排序链表中的重复元素 II
# Definition for singly-linked list.

# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummyH = ListNode(-999)
        dummyH.next = head
        preVal = head.val
        pre = dummyH
        cur = dummyH.next
        while (cur is not None) & (cur.next is not None):
            if cur.next.val > cur.val:
                pre = cur
                cur = cur.next

            elif cur.next.val =
                cur = ne.next

        return dummyH.next= cur.val:
                ne = cur.next

                while (ne.next is not None) & (ne.next.val ==cur.val):
                    ne = ne.next
                pre.next = ne.next