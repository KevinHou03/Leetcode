# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth = -1
        self.lm_value = None

        def dfs(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.lm_value = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return self.lm_value
