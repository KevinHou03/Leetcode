# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0, head)
        tracker = dummy

        while True:
            kth  = self.get_kth(tracker, k)
            if not kth:
                break
            follower = kth.next
            #tracker 在队伍之前，follower在队伍之后

            #now reverse the group
            prev, cur = kth.next, tracker.next
            while cur != follower:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            tmp = tracker.next
            tracker.next = kth
            tracker = tmp

        return dummy.next

    def get_kth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
