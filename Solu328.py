# 328. 奇偶链表
#
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if (head.next) is None:
            return head
        if (head.next.next) is None:
            return head
        last0 = head
        first1 = head.next
        last1 = head.next
        cur = head.next.next
        while(cur is not None):
            nextNode = cur.next
            last0.next = cur
            cur.next = first1
            last1.next = nextNode
            if nextNode is not  None:
                last1 = last1.next
                cur = last1.next
                last0 = last0.next
            cur = last1.next


        return head

asdf = ListNode(3)
print(asdf)