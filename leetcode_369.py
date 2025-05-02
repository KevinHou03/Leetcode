class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(head):
            dummy = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = dummy
                dummy = cur
                cur = temp
            return dummy

        new_head = reverse(head)
        cur = new_head
        while cur:
            if cur.val < 9:
                cur.val += 1
                break
            else:
                cur.val = 0
                if not cur.next:
                    cur.next = ListNode(1)
                    break
                cur = cur.next

        return reverse(new_head)





