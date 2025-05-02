class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # s = set()
        # A = headA
        # B = headB
        # while A and A.next:
        #     s.add(A)
        #     A = A.next
        # while B and B.next:
        #     if B in s:
        #         return B
        #     B = B.next
        A, B = headA, headB
        while A and B:
            if A == B:
                return headA
            if A  is None:
                A = headA
            if B is None:
                B = headB
        return None

