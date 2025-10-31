from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        match_nums = set(nums)
        while head and head.val in match_nums:
            head = head.next
        if head is None:
            return None
        prev = head
        next = prev.next
        while next:
            if next.val in match_nums:
                prev.next = next.next
                next = prev.next
            else:
                prev = next
                next = next.next
        return head


def generate_listnodes(arr_in):
    head = ListNode(arr_in[0])
    cur = head
    for i in range(1, len(arr_in)):
        cur.next = ListNode(arr_in[i])
        cur = cur.next
    return head


def print_listnodes(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


soln = Solution().modifiedList
print(
    f"{print_listnodes(soln([1,2,3],generate_listnodes([1,2,3,4,5])))} should be [4,5]"
)
print(
    f"{print_listnodes(soln([1],generate_listnodes([1,2,1,2,1,2])))} should be [2,2,2]"
)
