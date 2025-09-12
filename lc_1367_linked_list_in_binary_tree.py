from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: Optional[TreeNode]) -> bool:
        # IDEA: find all elements with matching first value, then check their children and exclude 'em until we either (1) finish
        # the linkedlist or (2) exhaust possible node paths.
        # Note that the number of node paths can actually *increase*, as two branches can be partially valid.
        # Probably most memory-efficient to do DFS just once, returning immediately if we find a happy path... however, this would
        # require spinning up multiple DFSs at the same time
        # So, we'll instead collect all possible start nodes in O(n) time, then dfs on them individually to disqualify.
        first_match_nodes = []

        def dfs_to_matching_firsts(node_in):
            if node_in is None:
                return
            if node_in.val == head.val:
                first_match_nodes.append(node_in)
            dfs_to_matching_firsts(node_in.left)
            dfs_to_matching_firsts(node_in.right)

        dfs_to_matching_firsts(root)

        # Now we'll move along each and check the match.
        def check_matching_path(list_node, tree_node):
            if tree_node is None and list_node is not None:
                return False
            if list_node is None:
                return True
            if list_node.val != tree_node.val:
                return False
            left_result = check_matching_path(list_node.next, tree_node.left)
            right_result = check_matching_path(list_node.next, tree_node.right)
            return left_result or right_result

        for i in range(len(first_match_nodes)):
            path_result = check_matching_path(head, first_match_nodes[i])
            if path_result is True:
                return True
        return False
