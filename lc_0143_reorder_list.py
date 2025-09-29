from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printvals(head):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # IDEA: Node stack from middle on. For sake of ease, we'll take elements in the
        # stack to be everything beyond len(listnodes) // 2
        # O(n) to find length, then O(n) to add to stack, then O(n) to zip.
        # Space is likewise O(n)
        fast = head
        slow = head
        lag = head
        while fast and fast.next:
            if fast != slow:
                lag = lag.next
            fast = fast.next.next
            slow = slow.next  # type: ignore
        lag.next = None
        node_stack = []
        node = slow
        while node:
            node_stack.append(node)
            node = node.next
        # Now we merge
        left = head
        while node_stack:
            right = left.next
            left.next = node_stack.pop()
            left.next.next = right
            if right is None and node_stack:
                left.next.next = node_stack.pop()
                left.next.next.next = None
                # printvals(head)
                return
            left = right
        # printvals(head)


def ln(vals, i):
    if i == len(vals):
        return None
    node = ListNode(vals[i])
    node.next = ln(vals, i + 1)
    return node


Solution().reorderList(ln([1, 2, 3, 4], 0))
Solution().reorderList(ln([1, 2, 3, 4, 5], 0))
