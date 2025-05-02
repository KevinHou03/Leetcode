class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next:
            if cur.next.val < cur.val:
                cur = cur.next
            else:
                insert = cur.next

                # 把cur和下一个连接起来，跳过cur.next也就是这个insert
                cur.next = insert.next

                prev = dummy
                while prev.next.val < insert.val:
                    prev = prev.next
                insert.next = prev.next
                prev.next = insert

        return dummy.next


                    # 2479  -> 8
