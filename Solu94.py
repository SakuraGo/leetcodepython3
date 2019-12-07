
#94. 二叉树的中序遍历
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def __init__(self, x):
        self._st = []
        self._res = []

    def addNodeToStack(self,node:TreeNode):

        if node.left is not None:
            self.addNodeToStack(node.left)
        self._res.append(node.val)
        if node.right is not None:
            self.addNodeToStack(node.right)


        return

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self._res
        self.addNodeToStack(root)
        return self._res
#非递归写法。。
# class Solution {
#         public List<Integer> inorderTraversal(TreeNode root) {
#             List<Integer> list = new ArrayList<>();
#             Stack<TreeNode> stack = new Stack<>();
#             TreeNode cur = root;
#             while (cur != null || !stack.isEmpty()) {
#                 if (cur != null) {
#                     stack.push(cur);
#                     cur = cur.left;
#                 } else {
#                     cur = stack.pop();
#                     list.add(cur.val);
#                     cur = cur.right;
#                 }
#             }
#             return list;
#         }
#     }
abc = [1,2]
abc.pop()
abc.append(3)
print(abc)

