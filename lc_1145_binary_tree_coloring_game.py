from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """
        Idea:
         - Since the players can only color unchosen nodes, this is really a question like:
          - If I cut them off by taking the parent, can I get the majority?
          - If I cut them off by taking either child, can I get the majority?
          We're gonna have to do a search for the match. We're also going to need to determine how many nodes are children. Thus, I think we should do DFS (O(n)) to find the val. Once there, we take this node and establish the number of children in its left and right subtrees. Then we have all the info we need to determine if we can pick a majority. We'll need O(n) time and O(H) space, where H is the height of the tree.
        """

        def find_match(node: Optional[TreeNode]):
            if node is None or node.val == x:
                return node
            left_res = find_match(node.left)
            return left_res if left_res is not None else find_match(node.right)

        def count_children(node: Optional[TreeNode]):
            if node is None:
                return 0
            return 1 + count_children(node.left) + count_children(node.right)

        matching_node = find_match(root)
        opp_l_children, opp_r_children = count_children(
            matching_node.left
        ), count_children(matching_node.right)
        parent_accessible = n - opp_l_children - opp_r_children - 1
        if any(
            [
                opp_l_children > (n // 2),
                opp_r_children > (n // 2),
                parent_accessible > (n // 2),
            ]
        ):
            return True

        return False
