# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Leetcode.leetcode_92 import ListNode


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 使用递归的话，每次返回的是一个已经完成的列表的head，可以注意到：
        # 这个已经完成的列表一定是递减的。。。
        # 首先用递归——>到链表的尾部，然后在回来，如果当前val > 返回的val, 则返回新head, else，直接返回return的node，就当跳过了当前node
        def helper(head):
            # 递归终止条件
            if not head:
                return None
            new_head = helper(head.next)
            if head.val < new_head.val:
                return new_head
            else:
                head.next = new_head
                return head

        return helper(head)

    # 方法2: 先翻转，再一次性遍历，维持一个cur_max记录当前最大值，如果比这个值小的话就删掉

     # 8 3 13 2 5
    def removeNodes_non_recur(self, head):
        def reverse(head):# 首先实现翻转一个列表
            dummy = None
            cur = head
            while cur:
                next_cur = cur.next
                cur.next = dummy
                dummy = cur
                cur = next_cur
            return dummy
        # reverse
        head = reverse(head)
        # 一次性遍历
        # none 8 13 2
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        cur_max = float('-inf')
        while cur:
            if cur.val > cur_max:
                cur_max = cur.val
                cur = cur.next
                prev = prev.next
            else:
                next_node = cur.next
                prev.next = next_node
                cur = next_node

        return reverse(prev.next)


