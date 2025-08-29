# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recurse(node):
    # returns a max length and a current depth
    if not node:
        return 0,-1
    length_left,depth_left = recurse(node.left)
    length_right,depth_right = recurse(node.right)
    return max(max(length_left,length_right),depth_left + depth_right + 2),max(depth_left,depth_right)+1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return recurse(root)[0]