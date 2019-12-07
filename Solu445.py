# 445. 两数相加 II
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
#  
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 进阶:
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        node1 = l1
        node2 = l2
        while node1 is not None:
            num1 += str(node1.val)
            node1 = node1.next

        while node2 is not None:
            num2 += str(node2.val)
            node2  = node2.next

        summ = int(num1) + int(num2)
        resDummy = ListNode(-1)
        res = resDummy
        for c in str(summ):
            res.next = ListNode(int(c))
            res = res.next

        return resDummy.next

'''
执行用时 : 80 ms , 在所有 Python 提交中击败了 68.22% 的用户 内存消耗 : 11.9 MB , 在所有 Python 提交中击败了 22.22% 的用户

假如不允许改原来的链表，就先copy一份短的链表，并且在这个copy的短链表前边补0，得到俩一样长的链表。 然后用递归。
##硬刚+递归法。。
class Solution(object):    
    def __add(self, l1, l2):
        if not l1 and not l2:
            return (0, None)  #carry, lowerNumList
        else:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            nextL1 = l1.next if l1 else None
            nextL2 = l2.next if l2 else None
            carry, lowerNumList = self.__add(nextL1, nextL2)
            listNode = ListNode((num+carry)%10)
            listNode.next = lowerNumList 
            return (int((num+carry)/10), listNode)
        
    def __getListLen(self, l):
        length = 0
        iterNode = l
        while iterNode:
            length += 1
            iterNode = iterNode.next
        return length
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lenL1 = self.__getListLen(l1)
        lenL2 = self.__getListLen(l2)
        maxLen, minLen, minList, maxList = (lenL1, lenL2, l2, l1) if lenL1 > lenL2 else (lenL2, lenL1, l1, l2)
        zfillList = None
        iterNode = zfillList
        iterMinNode = minList
        for i in range(0, maxLen):
            nextNode = None
            if maxLen-minLen > i:
                nextNode = ListNode(0) 
            else:
                nextNode = ListNode(iterMinNode.val)
                iterMinNode = iterMinNode.next
            if zfillList is None:
                zfillList = nextNode
                iterNode = zfillList
            else:
                iterNode.next = nextNode
                iterNode = nextNode
        carry, listNode = self.__add(maxList, zfillList)
        header = listNode
        if carry > 0:
            header = ListNode(carry)
            header.next = listNode
        return header

'''








        return l1


z = 0
print(str(z))