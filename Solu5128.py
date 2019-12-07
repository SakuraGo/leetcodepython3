# 5128. 最深叶节点的最近公共祖先
# 给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。
#
# 回想一下：
#
# 叶节点 是二叉树中没有子节点的节点
# 树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1
# 如果我们假定 A 是一组节点 S 的 最近公共祖先，
# 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self._res = None
        self._maxDep = 0
        self._memo = {}


    def bianliTree(self,node:TreeNode,depth:int):  ##单向 向下遍历，统计各层叶子结点个数
        if node.left is None and node.right is None:
            if depth in self._memo.keys():
                self._memo[depth] += 1
            else:
                self._memo[depth] = 1
            return

        if node.left is not None:
            self.bianliTree(node.left,depth+1)
        if node.right is not None:
            self.bianliTree(node.right,depth+1)

    def getRes(self,node:TreeNode,target:int,depth:int,targetDep:int):
        if node.left is None and node.right is None:
            if target == 1 and depth >= self._maxDep:
                self._res = node
                self._maxDep = depth
            if depth == targetDep:

                return node,1
            else:
                return node,0
        sum = 0
        if node.left is not None:
            node.left,leftSum = self.getRes(node.left,target,depth+1,targetDep)
            sum+=leftSum
        if node.right is not None:
            node.right, rightSum = self.getRes(node.right,target,depth+1,targetDep)
            sum += rightSum
        if sum == target and depth >= self._maxDep:
            self._res = node
            self._maxDep = depth
        return node,sum

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:


        self.bianliTree(root,0)
        leaves = [item for item in self._memo.items()]
        leaves.sort(key=lambda x:x[0],reverse=True)
        cnt = leaves[0][1]
        dep = leaves[0][0]
        self.getRes(root,cnt,0,dep)
        return self._res



rrr = TreeNode(1)
rrr.left = TreeNode(2)
rrr.left.left = TreeNode(4)
rrr.right = TreeNode(3)
qwer = Solution().lcaDeepestLeaves(rrr)
print(qwer.val)


''' 
     ### 反面教材 ，考虑的是所有叶子节点的公共节点。。。返回的一定是root
    def bianliTree(self, node: TreeNode):
        if node.left is None and node.right is None:

            return node, 1  # node，含叶子个数
        sum = 0
        if node.left is not None:
            node.left, leftCnt = self.bianliTree(node.left)
            sum += leftCnt
        if node.right is not None:
            node.right, rightCnt = self.bianliTree(node.right)
            sum += rightCnt

        return node, sum

    def searTree(self, node: TreeNode,target:int,depth:int):
        if node.left is None and node.right is None:
            #node.val = 1
            if target == 1 and depth > self._maxDep:
                print("buyinggai")
                self._maxDep = depth
                self._res = node
            return node, 1  # node，含叶子个数
        sum = 0
        if node.left is not None:
            node.left, leftCnt = self.searTree(node.left,target,depth+1)
            sum += leftCnt
        if node.right is not None:
            node.right, rightCnt = self.searTree(node.right,target,depth+1)
            sum += rightCnt
        if sum == target and depth>=self._maxDep:
            print("set111")
            self._maxDep = depth
            self._res = node

        return node, sum
'''