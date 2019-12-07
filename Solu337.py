#337. 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
# 输入: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \
#      3   1
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._memo = {}


    def rob(self, root: TreeNode) -> int:
        if (root is None):
            return 0
        if root in self._memo:
            return self._memo[root]

        if (root.left is None) & (root.right is None):
            print("yezi:"+root.val)
            self._memo[root] = root.val
            return root.val
        if root.right is None:
            max0 = self.rob(root.left)
            max1 = root.val + self.rob(root.left.left)+self.rob(root.left.right)
            print("reLeft:" + max(max0, max1))
            self._memo[root] = max(max0,max1)
            return max(max0,max1)
        if root.left is None:
            max2 = self.rob(root.right)
            max3 = root.val + self.rob(root.right.left) + self.rob(root.right.right)
            print("reRight:"+max(max2, max3))
            self._memo[root] = max(max2,max3)
            return  max(max2,max3)
        if (root.left is not None) & (root.right is not None):
            max4 = self.rob(root.left) + self.rob(root.right)
            max5 = root.val +  self.rob(root.left.left)+self.rob(root.left.right)
            + self.rob(root.right.left) + self.rob(root.right.right)
            print("Max:"+max(max4, max5))
            self._memo[root] = max(max4,max5)
            return max(max4,max5)

        return 1

# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         if root==None:
#             return 0
#         def helper(root):
#             if root==None:
#                 return [0,0]
#             left = helper(root.left)
#             right = helper(root.right)
#             rob = root.val + left[1] + right[1]
#             skip = max(left) + max(right)
#             print(left[1])
#             return [rob, skip]
#         res = helper(root)
#         return max(res)