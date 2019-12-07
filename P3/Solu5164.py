# 5164. 从链表中删去总和值为零的连续节点

# 给你一个链表的头节点
# head，请你编写代码，反复删去链表中由
# 总和
# 值为
# 0
# 的连续节点组成的序列，直到不存在这样的序列为止。
#
# 删除完毕后，请你返回最终结果链表的头节点。
#
#
#
# 你可以返回任何满足题目要求的答案。
#
# （注意，下面示例中的所有序列，都是对
# ListNode
# 对象序列化的表示。）

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        dummy  = ListNode(1133)
        dummy.next = head
        if head is None:
            return head
        print("head", head.val)
        p = dummy.next
        pre = dummy
        memoDic = {}

        flag  = False
        while p is not  None:
            val = p.val
            print(val)
            if val == 0:
                p = p.next
                pre.next = p
                continue

            if -val in memoDic.keys():
                ##改变了
                flag = True
                node = memoDic[-val]
                node.next = p.next
                break
            else:
                ##没改变
                items = list(memoDic.items())
                updatedItems = [(val+p.val,nod) for (val,nod) in items]
                updatedItems.append((p.val,pre))

                pre = p
                p = p.next
                memoDic = dict((updatedItems))
        # print(dummy.next)
        if flag is True:
            return self.removeZeroSumSublists(dummy.next)
        else:
            return dummy.next

# lis = [1,2,3]
# ss = [num+3 for num in lis]
# print(ss)
# ss += [555]
# print(ss)

hedd = ListNode(1)
hedd.next = ListNode(2)
hedd.next.next = ListNode(-3)
hedd.next.next.next = ListNode(3)
hedd.next.next.next.next = ListNode(1)

resHead = Solution().removeZeroSumSublists(hedd)

print(resHead)
