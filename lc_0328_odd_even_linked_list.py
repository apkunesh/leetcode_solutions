from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        even_head = head.next
        curr_odd, curr_even = head, even_head
        while curr_even:
            next_even = curr_even.next.next if curr_even.next else None
            next_odd = curr_odd.next.next if curr_odd.next else None
            curr_even.next = next_even
            if next_odd is None:
                curr_odd.next = even_head
                return head
            curr_odd.next = next_odd
            curr_odd, curr_even = next_odd, next_even
        curr_odd.next = even_head
        return head


def extract_all(node) -> List[int]:
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res


def gen_nodes(list_in) -> ListNode:
    head = ListNode(list_in[0])
    cur_node = head
    for i in range(1, len(list_in)):
        cur_node.next = ListNode(list_in[i])
        cur_node = cur_node.next
    return head


soln = Solution().oddEvenList
print(f"{extract_all(soln(gen_nodes([1, 2, 3, 4, 5])))} should be [1, 3, 5, 2, 4]")
print(
    f"{extract_all(soln(gen_nodes([2, 1, 3, 5, 6, 4, 7])))} should be [2, 3, 6, 7, 1, 5, 4]"
)
