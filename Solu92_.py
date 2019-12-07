class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        for i in range(1,m): ##定位要开始反串的位置
            pre = pre.next

        cur = pre.next

        for i in range(m,n): ##反串链表，cur，pre不动，把一个个nex丢到cur前面。。
            nex = cur.next
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex


        return dummy.next