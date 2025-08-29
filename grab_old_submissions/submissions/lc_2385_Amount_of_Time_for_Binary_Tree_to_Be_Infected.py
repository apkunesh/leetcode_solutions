# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # O(N) time. First we can find the start, then we can assess the distance between 
        # the start and all others; then the max of this is the time.
        # Easy part is find; how about distance? 
        # Note that this is equivalent to constructing a new graph w/ 3 as the root, then doing BFS to 
        # determine the maximum depth...
        # Basically, once we've found 3, we should recurse back "up" and set the distances of all parents,
        # all the way to the root. Then we should do DFS along all paths, setting the values of L and R children ONLY IF UNSET to be their parent's plus 1.
        def recurse_to_start(node):
            if not node:
                return None # Not found along this branch
            if node.val == start:
                node.dist = 0
                return node.dist
            left_dist = recurse_to_start(node.left)
            if left_dist is not None:
                node.dist = left_dist + 1
                return node.dist
            right_dist = recurse_to_start(node.right)
            if right_dist is not None:
                node.dist = right_dist + 1
                return node.dist
        
        recurse_to_start(root)

        global_max = {"max":0}
        def dfs(node, parent_dist): 
            # Now we go through and assess the distance for everybody, keeping track of global max
            if not node:
                return
            if not hasattr(node,"dist"):
                local_dist = parent_dist + 1
            else:
                local_dist = node.dist
            global_max["max"] = max(global_max["max"],local_dist)
            dfs(node.left,local_dist)
            dfs(node.right,local_dist)
        dfs(root,0)
        return global_max["max"]