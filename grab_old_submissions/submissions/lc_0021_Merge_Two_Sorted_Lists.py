# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            smaller = list1
            leftover = list2
        else:
            smaller = list2
            leftover = list1
        head = smaller
        target = smaller
        current_left = smaller.next
        current_right = leftover
        if not current_left:
            target.next = current_right
            return head
        while True:
            if current_left.val <= current_right.val:
                new_left = current_left.next
                target.next = current_left
                if not new_left:
                    current_left.next = current_right
                    return head
                current_left = new_left
            else:
                new_right = current_right.next
                target.next = current_right
                if not new_right:
                    current_right.next = current_left
                    return head
                current_right = new_right
            target = target.next