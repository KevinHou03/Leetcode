"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        '''
        inorder successor：
        如果有right child，找到right sub的left most
        如果没有，往parent找，直到找到一个left child
        '''

        if node.right:
            r_sub = node.right
            while r_sub.left:
                r_sub = r_sub.left
            return r_sub

        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent