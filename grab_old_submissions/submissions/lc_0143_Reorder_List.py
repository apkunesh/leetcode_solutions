# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # General idea: we'll reverse from the tail to the middle and "zip" them together.
        if not head or not head.next:
            return
        slow,fast =head,head
        before_slow = None
        while fast and fast.next:
            before_slow = slow
            fast = fast.next.next
            slow=slow.next
        if before_slow:
            before_slow.next = None
        # Lists are now separated into first half (smaller-or-equal) and right half (larger-or-equal)

        # Now we reverse everything, hanging onto the tail
        left = slow
        right = left.next
        left.next = None
        while right is not None:
            dummy = right.next
            right.next = left
            left = right
            right = dummy
        #Once we've run out, left is the tail.
        
        left_side = head
        right_side = left
        # Now we zip together, starting with the head.
        switch = 'right'
        curr = left_side
        left_side = left_side.next
        while right_side is not None or left_side is not None:
            if switch == 'left' and left_side is not None:
                curr.next = left_side
                left_side = left_side.next
                curr = curr.next
            elif switch == 'right' and right_side is not None:
                curr.next = right_side
                right_side = right_side.next
                curr = curr.next
            switch = 'right' if switch=='left' else 'left'
            
            