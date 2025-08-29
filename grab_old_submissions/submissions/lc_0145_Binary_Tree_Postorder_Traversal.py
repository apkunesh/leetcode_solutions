# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [[root,0]]
        results = []
        while stack:
            cur_vis = stack.pop()
            cur = cur_vis[0]
            vis = cur_vis[1]
            if vis == 0:
                stack.append([cur,1])
                if cur.right:
                    stack.append([cur.right,0])
                if cur.left:
                    stack.append([cur.left,0])
            else:
                results.append(cur.val)
        return results
