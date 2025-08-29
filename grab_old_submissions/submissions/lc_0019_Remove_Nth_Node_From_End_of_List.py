# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # did it, but this took way too many submissions. Would've helped me to draw out sooner.
    # Way sooner, in fact.
    # Also want to note that my soln was much-benefitted from the insight that n is the difference
    # between the "front" pointer and the node which will ultimately need to have its `next` updated.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        count = 0
        behind = None
        while cur.next:
            if behind:
                behind=behind.next
            cur=cur.next
            count+=1
            if count==n:
                behind = dummy
        behind.next = behind.next.next
        return dummy.next