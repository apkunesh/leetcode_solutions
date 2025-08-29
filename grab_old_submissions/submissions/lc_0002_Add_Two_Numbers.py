# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Idea: traverse until both are none. If the sum is more than 10, assign
        # the value of the sum node to ans-10 and note that we need to keep the 
        # 1 digit on the next time through
        # increment each node if it is not none
        # After increment, check if both are none; if they are, add an extra 1
        # if the stored extra indicates that we should.
        # Edge case: one is 0
        carry = False
        head = ListNode() #Empty
        cur_node = head 
        while l1 is not None or l2 is not None:
            l1_contrib = l1.val if l1 is not None else 0
            l2_contrib = l2.val if l2 is not None else 0
            carry_contrib = 1 if carry else 0
            tent_sum = l1_contrib+l2_contrib+carry_contrib
            if tent_sum>9:
                carry = True
                tent_sum-=10
            else:
                carry = False
            cur_node.next = ListNode(tent_sum)
            cur_node = cur_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and carry:
                cur_node.next = ListNode(1)
        return head.next
# TC: O(max(len(l1),len(l2)))
# SC: O(max(len(l1,len(l2)))), could be optimized to O(1) by overwriting l1 or l2


