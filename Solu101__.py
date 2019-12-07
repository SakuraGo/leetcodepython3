class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # def isDuiCheng(self, rt0 : TreeNode, rt1 : TreeNode):
    #     print(str(rt0.val)+"--"+str(rt1.val))
    #     if (rt0 is None ) & (rt1 is None):
    #         return True
    #     if (rt0 is not None) | (rt1 is not None):
    #         return  False
    #     if rt0.val != rt1.val:
    #         return False
    #
    #     return    (self.isDuiCheng(rt0.left ,rt1.right))&(self.isDuiCheng(rt0.right,rt1.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        q = [root.left,root.right]
        while len(q)>0:
            ll = q.pop()
            rr = q.pop()
            if (ll is None) & (rr is None):
                continue

            if (ll is None) | (rr is None):
                return False
            if ll.val != rr.val :
                return  False

            q.append(ll.left)
            q.append(rr.right)
            q.append(ll.right)
            q.append(rr.left)
        return True
'''
    class Solution {
    public int countNodes(TreeNode root) {
    / **
    完全二叉树的高度可以直接通过不断地访问左子树就可以获取
    判断左右子树的高度:
        如果相等说明左子树是满二叉树, 然后进一步判断右子树的节点数(最后一层最后出现的节点必然在右子树中)

    如果不等说明右子树是深度小于左子树的满二叉树, 然后进一步判断左子树的节点数(最后一层最后出现的节点必然在左子树中)
                            ** /
    if (root == null)
    return 0;
    int
    ld = getDepth(root.left);
    int
    rd = getDepth(root.right);
    if (ld == rd) return (1 << ld) + countNodes(root.right); // 1(根节点) + (1 << ld)-1(左完全左子树节点数) + 右子树节点数量
    else return (1 << rd) + countNodes(root.left); // 1(根节点) + (1 << rd)-1(右完全右子树节点数) + 左子树节点数量

}

private
int
getDepth(TreeNode
r) {
int
depth = 0;
while (r != null) {
depth++;
r = r.left;
}
return depth;
}
}
'''