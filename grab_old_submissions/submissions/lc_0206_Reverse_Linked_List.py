# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_node(left_node, right_node):
    if not right_node:
        return left_node
    next_node = right_node.next
    right_node.next = left_node
    print(f"Right node {right_node.val} now points to {left_node.val if left_node else None}")
    if next_node is None:
        return right_node
    return reverse_node(right_node, next_node)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverse_node(None,head)