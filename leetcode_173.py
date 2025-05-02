# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_left(root)  # Initialize with leftmost nodes

    def _push_left(self, node):
        """ Push all left children onto the stack """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()  # Get the next smallest element
        if node.right:
            self._push_left(node.right)  # Push left path of right subtree
        return node.val  # Return the in-order value

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0