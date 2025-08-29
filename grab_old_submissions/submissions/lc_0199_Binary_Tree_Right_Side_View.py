# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        rightmost_vals = []
        while len(queue) > 0:
            for i in range(len(queue)-1):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            print_node = queue.popleft()
            rightmost_vals.append(print_node.val)
            if print_node.left:
                queue.append(print_node.left)
            if print_node.right:
                queue.append(print_node.right)
        return rightmost_vals