# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Made a significant mistake in that I didn't update parent_val when moving to the left.
    # Made an even more significant mistake by neglecting to take into account minimum value.
    # Basically I assessed whether it was a heap, not a BST.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root,-10000000000,100000000000)]
        cur_node = None
        while cur_node or stack:
            if cur_node is None:
                cur_node, min_val,max_val = stack.pop()
            else:
                if cur_node.val <= min_val or cur_node.val >= max_val:
                    return False
                stack.append((cur_node.right,cur_node.val,max_val))
                max_val = cur_node.val
                cur_node = cur_node.left
        return True
