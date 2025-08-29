# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # It's intended that I do this iteratively. 
        stack = []
        cur = root
        results = []
        while cur or stack:
            #push right, point left
            if cur:
                results.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return results