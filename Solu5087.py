# 5087. 活字印刷  显示英文描述
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = 0
        memoDict = {}
        doubleStr = tiles + tiles+tiles
        lens = len(doubleStr)
        for charLen in range(1,len(tiles)+1):
            for  i in range(lens-charLen+1):
                subStr = doubleStr[i:i+charLen]
                print(subStr)
                memoDict[subStr] = 1

        return len(memoDict.keys())


str = "AAABBC"
test = Solution().numTilePossibilities(str)

# class Solution {
#     public int numTilePossibilities(String tiles) {
#         HashSet<String> set = new HashSet<>();
#         numTilePossibilities(tiles.toCharArray(), new StringBuilder(), set);
#         return set.size();
#     }
#
#     public void numTilePossibilities(char[] chars, StringBuilder build, HashSet<String> set) {
#         if (build.length() > 0) set.add(build.toString());
#         for(int i = 0; i < chars.length; i++) {
#             char x = chars[i];
#             if (x > 0) {
#                 build.append(x);
#                 chars[i] = 0;
#                 numTilePossibilities(chars, build, set);
#                 build.deleteCharAt(build.length()-1);
#                 chars[i] = x;
#             }
#         }
#     }
# }

## 二叉树
# # 5084. 根到叶路径上的不足节点  显示英文描述
# 题目难度 Medium
# 给定二叉树的根 root，考虑所有从根到叶的路径：从根到任何叶的路径。 （叶节点是没有子节点的节点。）
#
# 如果交于节点 node 的每个根到叶路径的总和严格小于限制 limit，则该节点为不足节点。
#
# 同时删除所有不足节点，并返回生成的二叉树的根。
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(node, sum_):
            if not node:
                return sum_, sum_ >= limit
            sum_ += node.val
            left, lf = dfs(node.left, sum_)
            right, rf = dfs(node.right, sum_)
            if not lf:
                node.left = None
            if not rf:
                node.right = None
            path_sum = max(left, right)
            return path_sum, path_sum >= limit
        sum_, flag = dfs(root, 0)
        if not flag:
            return None
        return root
# 5086. 不同字符的最小子序列  显示英文描述
# 用户通过次数 50
# 用户尝试次数 122
# 通过次数 53
# 提交次数 211
# 题目难度 Medium
# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。
# 输入："cdadabcc"
# 输出："adbc"
# from collections import Counter
# class Solution(object):
#     def smallestSubsequence(self, text):
#         """
#         :type text: str
#         :rtype: str
#         """
#         cnts = Counter(text)
#         stack = []
#         visited = set()
#         for c in text:
#             if c in visited:
#                 cnts[c] -= 1
#                 continue
#             while stack and c < stack[-1] and cnts[stack[-1]]:
#                 item = stack.pop()
#                 visited.remove(item)
#             cnts[c] -= 1
#             visited.add(c)
#             stack.append(c)
#         return ''.join(stack)