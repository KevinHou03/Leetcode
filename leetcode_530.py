# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # res = float('inf')
        # cur = root
        #
        # def dfs(node, cur_min):
        #     if not node:
        #         return float('inf')
        #
        #     left_val = node.left if node.left.val else float('inf')
        #     right_val = node.right if node.right.val else float('inf')
        #
        #     min_diff = min(abs(node.val - left_val), abs(node.val - right_val))
        #     cur_min = min(cur_min, min_diff)
        #
        #     return cur_min
        #
        # return dfs(root, res)
        #

        # inorder traversal


        #         # 利用中序遍历从小到大的性质进行search

        #  nonlocal不适用的话可以用dict或者list储存 prev和mindiff两个变量！！
        min_diff = float('inf')
        prev = None
        def in_order(node):
            nonlocal min_diff, prev
            if not node:
                return
            in_order(node.left)
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
            in_order(node.right)

        in_order(root)
        return min_diff






