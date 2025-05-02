class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        cur = head
        while cur and cur.next:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False