# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(0, left_max)
            right_max = max(0, right_max)

            res[0] = max(res[0], node.val + left_max + right_max) #最大值更新为一整条路径的最大值 左 - node - 右

            return node.val + max(left_max, right_max)#返回只能返回不分叉的，因为作为left/right sub sum肯定是不能分叉的

        dfs(root)
        return res[0]

