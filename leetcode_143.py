class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # find mid-point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # now you have 2 linked list, reverse the 2nd onel and merge them

        # reverse it, when end
        prev = None
        cur = head2
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # merge, first, second are the head of two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2










