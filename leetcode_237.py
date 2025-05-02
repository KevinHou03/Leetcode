class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 没有head的access，我们只能把next的value copy到current来
        # 1 -> 2 -> "4" -> 5 -> 6 -> 7 -> 7
        prev = node
        next = node.next
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None

'''
1 2 3 4 5 6
13524
'''
