# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head,head
        found = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                found = True
                break
        if not found:
            return None
        meeter = head
        while meeter != slow:
            meeter = meeter.next
            slow = slow.next
        return meeter