from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_listnodes(values):
    head = ListNode(values[0])
    cur_node = head
    for i in range(1, len(values)):
        next_node = ListNode(values[i])
        cur_node.next = next_node
        cur_node = cur_node.next
    return head


def reverse_section(prev_left: Optional[ListNode], cur_node: ListNode, k):
    next_start = cur_node
    for i in range(k):
        if next_start is None:
            if prev_left is not None:
                prev_left.next = cur_node
            return (
                None,
                None,
            )  # Remaining list is too short to reverse #TODO: Outer should handle on this
        next_start = next_start.next
    l = cur_node
    next_l = l
    r = cur_node.next
    l.next = None  #
    for i in range(k - 1):
        next_r = r.next
        r.next = l
        l = r
        r = next_r
    if prev_left is not None:
        prev_left.next = l
    return next_l, next_start


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        grand_head = head
        for i in range(k - 1):
            if grand_head is None:
                return head
            grand_head = grand_head.next
        outer_l = None
        outer_start = head
        while outer_start is not None:
            outer_l, outer_start = reverse_section(outer_l, outer_start, k)
        return grand_head


def return_values(node: ListNode):
    next_node = node
    all_values = []
    while next_node is not None:
        all_values.append(next_node.val)
        next_node = next_node.next
    return all_values


first_head = generate_listnodes([1, 2, 3, 4, 5])
after_reverse = Solution().reverseKGroup(first_head, 2)
print(return_values(after_reverse))

second_head = generate_listnodes([1, 2, 3, 4, 5])
after_reverse = Solution().reverseKGroup(second_head, 3)
print(return_values(after_reverse))
