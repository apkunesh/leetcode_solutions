# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(node_1,node_2):
    # case 1: both nodes are None
    if node_1 is None and node_2 is None:
        return True
    # case 2: one node is none, other exists
    if (node_1 is None and node_2 is not None) or (node_2 is None and node_1 is not None):
        return False
    # case 3: both nodes exist, values differ
    if node_1.val != node_2.val:
        return False
    # Recursive case: check left and right subtrees
    left_recurse = recurse(node_1.left,node_2.left)
    if left_recurse is False:
        return False
    right_recurse = recurse(node_1.right,node_2.right)
    if right_recurse is False:
        return False
    return True

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return recurse(p,q)