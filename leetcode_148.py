# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def sort(head):
            if not head or not head.next:
                return head

            middle = get_middle(head)
            head2 = middle.next
            middle.next = None

            left = sort(head)
            right = sort(head2)

            res = merge(left, right)
            return res

        def get_middle(head):
            fast, slow = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left.val <= right.val:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)
            return result

        return sort(head)