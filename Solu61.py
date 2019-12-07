# 61. 旋转链表
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k < 1:
            return head
        dataLis = []

        cur = head
        while cur is not None:
            dataLis.append(cur)
            cur = cur.next
        lenn = len(dataLis)
        if lenn == 0:
            return  head
        bias = k%lenn

        if bias == 0:
            return head
        resDummy = ListNode(0)
        resCur = resDummy
        for node in dataLis[-bias:]:
            print(node.val)
            resCur.next = node
            resCur = resCur.next
        print("aaa")
        for node in dataLis[:-bias]:
            print(node.val)
            resCur.next = node
            resCur = resCur.next
        resCur.next = None
        return resDummy.next

'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        jishu = result = head
        len = 0
        while jishu and jishu.next:
            len += 1
            jishu = jishu.next
        len += 1
        jishu.next = head
        rot = k % len
        for i in range(0, len - rot):
            pre = result
            result = result.next
        pre.next = None
        return result

'''

aaa= ListNode(1)
aaa.next = ListNode(2)
# aaa.next.next = ListNode(3)
# aaa.next.next.next = ListNode(4)
# aaa.next.next.next.next = ListNode(5)
aaa.next.next =aaa
# res = Solution().rotateRight(aaa,2)
print("asd")