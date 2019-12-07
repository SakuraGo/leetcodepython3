# Definition for singly-linked list.
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(-9999)
        dummy.next = head
        pre = dummy
        index = 0
        while index<m-1:
            pre = pre.next
            print(index)
            index+=1

        ##理论上是O（n）复杂度。但是超时了？
        preMark = pre #标记m前的点

        index = m
        cur = preMark.next
        curMark =  cur #标记m位置的点
        nex = cur.next
        while index<=n:
            cur.next = pre
            pre = cur
            cur = nex
            if cur.next is not None:
                nex = cur.next
            print(index)
            index +=1

        preMark.next = pre

        curMark.next = cur
        print(dummy.next)
        return dummy.next

a = ListNode(3)
a.next = ListNode(5)
Solution().reverseBetween(a,1,2)
