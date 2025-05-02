# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def largestValues(root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []
        queue = deque([root])
        # 用一个for loop就可以pop掉一层，再加一层
        while queue:
            max_val = float('-inf')
            level_size = len(queue)
            for i in range(level_size):
                cur_val = queue.popleft()
                if cur_val > max_val:
                    max_val = cur_val

                if cur_val.left:
                    queue.append(cur_val.left)
                if cur_val.right:
                    queue.append(cur_val.right)
            res.append(max_val)

        return res


