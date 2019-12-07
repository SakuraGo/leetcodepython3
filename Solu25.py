# 25. K 个一组翻转链表
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:



    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy .next = head
        index = 0
        cur = dummy
        while index < k:
            if  cur is None or cur.next is None:
                return head
            else:
                cur = cur.next
                index+=1
        final = cur
        nextHead = final.next
        pre = dummy
        cur = dummy.next
        nex = cur.next
        while pre is not final:
            cur.next = pre
            pre = cur
            cur = nex
            if nex is not None:
                nex = nex.next
        dummy.next = final
        head.next = self.reverseKGroup(nextHead,k)
        return dummy.next


