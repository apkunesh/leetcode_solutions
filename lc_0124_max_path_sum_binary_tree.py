from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(h) memory for call stack, O(n) time
        # Iteratively would kinda suck.
        global_max = {"max": -2 * 10**32}

        def recurse(node: Optional[TreeNode]):
            # Returns pathmax, pathright after updating global_max.
            if node is None:
                return 0
            left_contrib = recurse(node.left)
            right_contrib = recurse(node.right)
            global_max["max"] = max([global_max["max"], left_contrib + node.val + right_contrib])  # type: ignore
            return max(
                [left_contrib + node.val, right_contrib + node.val, 0]
            )  # If there's no positive sum, best to just not include.

        recurse(root)
        return global_max["max"]
