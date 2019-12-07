# 589. N叉树的前序遍历
# 给定一个 N 叉树，返回其节点值的前序遍历。

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from typing import List

class Solution:
    def __init__(self):
        self._res = []

    def preO(self,node:Node):
        if node ==None:
            return
        self._res.append(node.val)
        for chi in node.children:
            self.preO(chi)


    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return self._res
        self.preO(root)

        return self._res

'''
class Solution:
    def postOrder(self, root: Node):
        list = []
        if root is None:
            return list
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)                   #pop(-1)表示出栈，弹出栈顶元素
            list.append(node.val)
            if node.children:
                length = len(stack)                #记录栈的元素个数
                for child in node.children:
                    stack.insert(length, child)    #把孩子节点插入length的位置，相当于倒序插入
        return list
'''

