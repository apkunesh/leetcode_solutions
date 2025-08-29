# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(node):
    if not node:
        return 0
    left = recurse(node.left)
    if left is False:
        return False
    right = recurse(node.right)
    if right is False:
        return False
    if abs(right-left) > 1:
        return False
    return max(left,right)+1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = recurse(root)
        return False if result is False else True