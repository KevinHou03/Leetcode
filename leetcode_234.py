class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.val != stack.pop():
                return False
            cur = cur.next
        return True
