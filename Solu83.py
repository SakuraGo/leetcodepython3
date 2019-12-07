# 83. 删除排序链表中的重复元素
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:  ## 别忘了递归终止条件。。
            return None
        if head.next is None:  ## 别忘了递归终止条件。。
            return head
        if head.next.val == head.val:
            head = self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head

'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            if head.next == None:
                return head
            else:
                #cur = head.next
                head2 = self.deleteDuplicates(head.next)
                if head2.val == head.val:
                    try:
                        head.next = head2.next
                        return head
                    except:
                        return head
                else:
                    head.next = head2
                    return head
        else:
            return head
'''