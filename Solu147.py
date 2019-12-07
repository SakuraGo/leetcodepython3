# 147. 对链表进行插入排序
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

import sys

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-9999999)
        if head is None:
            return head
        cur = head
        finNode = dummy

        while cur is not None:
            print("ccc:%s"%cur.val)
            pre = dummy
            compNode = dummy
            flag = dummy
            ##寻找要插入的点 flag
            while compNode is not None:
                #print(compNode.val)
                if compNode.next is None and compNode.val< cur.val:
                    #compNode.next = cur
                    flag = compNode
                    break
                elif compNode.val < cur.val:
                    pre = compNode
                    compNode = compNode.next
                elif  compNode.val >= cur.val:
                    # pre.next = cur
                    flag = pre
                    break
            print(flag.val)
            ##穿针引线操作
            if flag.next is None:
                curNex = cur.next
                flag.next = cur
                finNode = cur
                cur.next = None
                # if curNex is not None:
                cur = curNex

            else:
                nex = flag.next
                curNex = cur.next
                flag.next = cur
                cur.next = nex
                # finNode.next = curNex
                # if curNex is not None:
                cur = curNex

        return dummy.next

testN = ListNode(3)
testN.next = ListNode(2)
testN.next.next = ListNode(4)
# testN.next.next.next = ListNode(3)

res  = Solution().insertionSortList(testN)
print(res)


'''
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #naive
        nodeList = []
        while(head):
            nodeList.append(head)
            head = head.next
        nodeList.sort(key=lambda x:x.val)
        dummy = ListNode(0)
        pre = dummy
        for node in nodeList:
            pre.next = node
            pre = node
        pre.next = None
        return dummy.next
    
'''