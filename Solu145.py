# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        staccc = [root]
        cur = root
        res = []
        while (cur is not None ) | (len(staccc)>0):
            if (cur is not None):
                if (cur.left is None ) & (cur.right is None):
                    print("+++"+str(cur.val))
                    res.append(cur.val)
                    staccc.pop()
                    if len(staccc) > 0:
                        cur = staccc[-1]
                    else:
                        break
                else:
                    fat = cur
                    staccc.append(cur.right)
                    staccc.append(cur.left)
                    cur = cur.left
                    fat.left = None  ##打断连接
                    fat.right = None
                    ##staccc.append(cur)
            else:
                staccc.pop()
                if len(staccc)>0:
                    cur = staccc[-1]

        return res