# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def same_tree(node_1,node_2):
    if node_1 is None and node_2 is None:
        return True
    if (node_1 is None and node_2 is not None) or (node_2 is None and node_1 is not None):
        return False
    if node_1.val != node_2.val:
        return False
    if same_tree(node_1.left,node_2.left) is True and same_tree(node_1.right,node_2.right) is True:
        return True
    return False

def recurse(root,subRoot):
    if same_tree(root,subRoot):
        return True
    if root.left is not None and recurse(root.left,subRoot) is True:
        return True
    if root.right is not None and recurse(root.right,subRoot) is True:
        return True
    return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Idea: do preorder DFS on root
        # For each node, do dfs starting from subroot to check for equality
        return recurse(root,subRoot)