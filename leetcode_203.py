class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            if cur.next.val == val:
                fuck = cur.next.next
                cur.next = fuck
            else:
                cur = cur.next
        return dummy.next


