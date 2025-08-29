# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recurse(tree_node):
    if tree_node is None:
        return
    dummy = tree_node.left
    tree_node.left = recurse(tree_node.right)
    tree_node.right = recurse(dummy)
    return tree_node

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        return recurse(root)        