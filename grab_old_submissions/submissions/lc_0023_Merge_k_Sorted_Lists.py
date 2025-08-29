# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two_lists(list1,list2):
    head = list1 if list1.val <= list2.val else list2
    top = list2 if list1.val <= list2.val else list1
    bottom = head
    bottom_right = bottom.next
    while True:
        if not top:
            return head
        if not bottom_right:
            bottom.next = top
            return head
        if bottom_right.val <= top.val:
            bottom = bottom_right
            bottom_right = bottom.next
        else:
            top_dummy = top.next
            bottom.next = top
            bottom = top
            top = bottom_right
            bottom_right = bottom.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_lists = [elem for elem in lists if elem is not None]
        while True:
            if len(all_lists) == 0:
                return None
            if len(all_lists) == 1:
                return all_lists[0]
            left_lists = all_lists[0::2]
            right_lists = all_lists[1::2]
            new_lists = []
            for left_list,right_list in zip(left_lists[0:len(right_lists)],right_lists):
                new_lists.append(merge_two_lists(left_list,right_list))
            if len(left_lists) != len(right_lists):
                new_lists.append(left_lists[-1])
            all_lists = new_lists