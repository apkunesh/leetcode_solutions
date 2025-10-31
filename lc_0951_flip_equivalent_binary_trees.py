# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Ways two nodes are not equivalent:
         - At least 1 value of the two children are not the same
         - If the two nodes have different values, any children do not match
         - If the two nodes have the same value, neither assignment satisfies that children match.
        """

        def recurse(node1, node2):
            if node1 is None and node2 is None:
                return True
            if (node1 is None and node2 is not None) or (
                node2 is None and node1 is not None
            ):
                return False
            if node1.val != node2.val:
                return False
            if (
                not node1.left
                and not node1.right
                and not node2.right
                and not node2.left
            ):
                # We're at leaves whose values match
                return True
            if (
                recurse(node1.left, node2.left) and recurse(node1.right, node2.right)
            ) or (
                recurse(node1.right, node2.left) and recurse(node1.left, node2.right)
            ):
                return True
            return False

        return recurse(root1, root2)
