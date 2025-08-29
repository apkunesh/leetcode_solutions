# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast,slow = head,head
        left_side = []
        while fast and fast.next:
            left_side.append(slow.val)
            slow = slow.next
            fast=fast.next.next
        middle_to_right = slow
        right_side = deque()
        while middle_to_right:
            right_side.append(middle_to_right.val)
            middle_to_right = middle_to_right.next
        grand_max = None
        for i in range(len(left_side)):
            grand_max = max(left_side.pop()+right_side.popleft(),grand_max) if grand_max is not None else left_side.pop()+right_side.popleft()
        return grand_max