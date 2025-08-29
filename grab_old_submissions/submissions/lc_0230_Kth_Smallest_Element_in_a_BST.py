# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Seems there should be a simpler way, but I'm not sure...
        self.index = 0
        self.k = k
        def traverse(root):
            if not root:
                return None
            left_result = traverse(root.left)
            if left_result:
                return left_result
            self.index+=1
            if self.k == self.index:
                return root.val
            right_result = traverse(root.right)
            if right_result:
                return right_result
        return traverse(root)